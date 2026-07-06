import os
from pathlib import Path

import torch
import lightning.pytorch as pl
from lightning.pytorch.callbacks import EarlyStopping, ModelCheckpoint
from lightning.pytorch.loggers import TensorBoardLogger
from lightning.pytorch.strategies import DDPStrategy
from torch.utils.data import Dataset, DataLoader
from model import ChemPFN
from features import get_featurizer, FEATURIZER, get_rdkit_descriptors

featurizer = get_featurizer(FEATURIZER)


class SmilesDataset(Dataset):
    def __init__(self, smiles_list, length=65_536):
        self.smiles_list = smiles_list
        self.length = length

    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        return idx


def make_collate_fn(smiles_list, desc_tensor, min_n=64, max_n=1_024):
    def collate_fn(batch):
        n_samples = torch.randint(min_n, max_n + 1, (1,)).item()
        idx = torch.randint(0, len(smiles_list), (n_samples,)).tolist()
        selected = [smiles_list[i] for i in idx]
        graph = featurizer(selected)
        descs = desc_tensor[idx]
        return graph, descs
    return collate_fn


def run_training(smiles_list, max_epochs=512, training_task="regression", init_from=None):
    print(f"=== Phase: {training_task} pre-training ===")
    print("Computing RDKit descriptors for training set...")
    raw_desc = get_rdkit_descriptors(smiles_list)
    print(f"Descriptor shape: {raw_desc.shape}")

    raw_t = torch.tensor(raw_desc, dtype=torch.float32)
    desc_mean = raw_t.mean(dim=0)
    desc_std = raw_t.std(dim=0) + 1e-6
    desc_tensor = (raw_t - desc_mean) / desc_std

    dataset = SmilesDataset(smiles_list)
    dataloader = DataLoader(
        dataset,
        batch_size=32,
        num_workers=2,
        shuffle=True,
        collate_fn=make_collate_fn(smiles_list, desc_tensor),
    )

    if init_from and Path(init_from).exists():
        print(f"Initializing from checkpoint: {init_from}")
        model = ChemPFN.load_from_checkpoint(init_from)
        model.hparams.training_task = training_task
    else:
        model = ChemPFN(training_task=training_task)

    logger = TensorBoardLogger(
        save_dir=f"logs/{training_task}/", default_hp_metric=False
    )

    early_stop_callback = EarlyStopping(
        monitor="train_loss_epoch",
        patience=20,
        mode="min",
        check_on_train_epoch_end=True,
    )
    model_checkpoint_callback = ModelCheckpoint(
        monitor="train_loss_epoch",
        dirpath=Path(logger.log_dir) / "checkpoints",
        filename="model-{epoch:02d}-{train_loss_epoch:.4f}",
        save_top_k=1,
        mode="min",
        save_on_train_epoch_end=True,
    )

    trainer = pl.Trainer(
        max_epochs=max_epochs,
        accelerator="auto",
        devices="auto",
        strategy=DDPStrategy(find_unused_parameters=True),
        logger=logger,
        callbacks=[early_stop_callback, model_checkpoint_callback],
        default_root_dir=logger.log_dir,
    )

    trainer.fit(model, dataloader)
    print(f"Phase {training_task} complete. Logs: {logger.log_dir}")

    return model_checkpoint_callback.best_model_path


if __name__ == "__main__":
    torch.autograd.graph.set_warn_on_accumulate_grad_stream_mismatch(False)

    pl.seed_everything(42)
    with open("cleaned_pubchem_1MM.smiles", "r") as file:
        smiles = [line.strip() for line in file.readlines()]

    # Phase 1: Regression pre-training from scratch
    reg_ckpt = run_training(smiles, max_epochs=512, training_task="regression")

    # Phase 2: Classification pre-training from scratch
    cls_ckpt = run_training(smiles, max_epochs=512, training_task="classification")

    print(f"Both phases complete.")
    print(f"  Regression checkpoint: {reg_ckpt}")
    print(f"  Classification checkpoint: {cls_ckpt}")

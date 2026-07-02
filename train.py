from pathlib import Path

import torch
import lightning.pytorch as pl
from lightning.pytorch.callbacks import EarlyStopping, ModelCheckpoint
from lightning.pytorch.loggers import TensorBoardLogger
from torch.utils.data import Dataset, DataLoader
from model import ChemPFN
from features import get_rdkit_features

class PFNSyntheticDataset(Dataset):
    def __init__(self, X_full, length=65_536):
        self.X_full = X_full
        self.length = length

    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        return idx  

def make_collate_fn(X_full, min_n=64, max_n=1_024):
    def collate_fn(batch):
        B = len(batch)
        n_samples = torch.randint(min_n, max_n + 1, (1,)).item()
        idx = torch.randint(0, len(X_full), (B, n_samples))
        return X_full[idx] 
    return collate_fn

def run_training(smiles_list, max_epochs=512):
    X_raw = get_rdkit_features(smiles_list)
    
    # RDKit Morgan count fingerprint features are exactly 2048 long based on features.py
    d_fp = 2048
    d_desc = X_raw.shape[1] - d_fp

    X_mean = torch.zeros(X_raw.shape[1], dtype=torch.float32)
    X_std = torch.ones(X_raw.shape[1], dtype=torch.float32)

    # IMPORTANT: Only calculate mean/std for continuous descriptors.
    # Normalizing count fingerprints ruins their integer properties.
    X_mean[:d_desc] = torch.tensor(X_raw[:, :d_desc].mean(axis=0), dtype=torch.float32)
    X_std[:d_desc] = torch.tensor(X_raw[:, :d_desc].std(axis=0) + 1e-6, dtype=torch.float32)

    # The descriptor portion is normalized (mean 0, std 1)
    # The fingerprint portion remains completely untouched
    X_normalized = (torch.tensor(X_raw) - X_mean) / X_std

    dataset = PFNSyntheticDataset(X_normalized)
    dataloader = DataLoader(
        dataset,
        batch_size=32,
        num_workers=2,
        shuffle=True,
        collate_fn=make_collate_fn(X_normalized),
    )

    model = ChemPFN(d_desc=d_desc, d_fp=d_fp)
    model.X_mean = X_mean
    model.X_std = X_std
    
    logger = TensorBoardLogger(save_dir="logs/", default_hp_metric=False)
    
    early_stop_callback = EarlyStopping(
        monitor="train_loss_epoch", 
        patience=10,
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
        logger=logger,
        callbacks=[early_stop_callback, model_checkpoint_callback],
        default_root_dir=logger.log_dir,
    )
    
    trainer.fit(model, dataloader)
    print(f"Training complete. Logs available in: {logger.log_dir}")

if __name__ == "__main__":
    torch.autograd.graph.set_warn_on_accumulate_grad_stream_mismatch(False)

    pl.seed_everything(42)
    with open("cleaned_pubchem_1MM.smiles", "r") as file:
        smiles = [line.strip() for line in file.readlines()]
    run_training(smiles)

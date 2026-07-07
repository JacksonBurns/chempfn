import os
from pathlib import Path

import torch
import lightning.pytorch as pl
from lightning.pytorch.callbacks import EarlyStopping, ModelCheckpoint
from lightning.pytorch.loggers import TensorBoardLogger
from lightning.pytorch.strategies import DDPStrategy
from torch.utils.data import Dataset, DataLoader

from model import ChemPFN

from model import featurizer



from lightning.pytorch.callbacks import Callback

class ContextWindowCurriculum(Callback):
    def __init__(self, collate_fn, warmup_epochs=256, start_max_n=128, end_max_n=4096):
        self.collate_fn = collate_fn
        self.warmup_epochs = warmup_epochs
        self.start_max_n = start_max_n
        self.end_max_n = end_max_n

    def on_train_epoch_start(self, trainer, pl_module):
        current_epoch = trainer.current_epoch
        
        # Linearly scale the maximum context window size
        if current_epoch < self.warmup_epochs:
            progress = current_epoch / self.warmup_epochs
            new_max_n = self.start_max_n + progress * (self.end_max_n - self.start_max_n)
            self.collate_fn.current_max_n = int(new_max_n)
        else:
            self.collate_fn.current_max_n = self.end_max_n
            
        # Log it to TensorBoard so you can track the curriculum
        pl_module.log("context_window_max", float(self.collate_fn.current_max_n), sync_dist=True)


class DelayedEarlyStopping(EarlyStopping):
    def __init__(self, start_tracking_epoch, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_tracking_epoch = start_tracking_epoch

    def on_train_epoch_end(self, trainer, pl_module):
        # Ignore tracking completely until the curriculum finishes
        if trainer.current_epoch < self.start_tracking_epoch:
            return
        
        # Once we reach the target epoch, resume normal tracking
        super().on_train_epoch_end(trainer, pl_module)

    def on_validation_end(self, trainer, pl_module):
        # Added just in case you ever switch to monitoring val_loss
        if trainer.current_epoch < self.start_tracking_epoch:
            return
        super().on_validation_end(trainer, pl_module)


class SmilesDataset(Dataset):
    def __init__(self, smiles_list, length=65_536):
        self.smiles_list = smiles_list
        self.length = length

    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        return idx


class CurriculumCollate:
    def __init__(self, smiles_list, min_n=64, start_max_n=128, end_max_n=4096):
        self.smiles_list = smiles_list
        self.min_n = min_n
        self.current_max_n = start_max_n
        self.end_max_n = end_max_n

    def __call__(self, batch):
        # Dynamically sample up to the *current* maximum context window
        n_samples = torch.randint(self.min_n, int(self.current_max_n) + 1, (1,)).item()
        idx = torch.randint(0, len(self.smiles_list), (n_samples,)).tolist()
        
        selected = [self.smiles_list[i] for i in idx]
        graph = featurizer(selected)
        
        return (graph,)


def run_training(smiles_list, max_epochs=512, training_task="regression", init_from=None):
    print(f"=== Phase: {training_task} pre-training ===")

    dataset = SmilesDataset(smiles_list)
    
    # 1. Instantiate the stateful collator
    collate_fn = CurriculumCollate(
        smiles_list, 
        min_n=64, 
        start_max_n=128,  # Start with a smaller ceiling 
        end_max_n=4096,    # Grow to your target ceiling
    )
    
    dataloader = DataLoader(
        dataset,
        batch_size=32,
        num_workers=1,
        shuffle=True,
        collate_fn=collate_fn, # 2. Use it here
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

    early_stop_callback = DelayedEarlyStopping(
        start_tracking_epoch=256,
        monitor="train_loss_epoch",
        patience=32,
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
    
    # 3. Instantiate the callback (e.g., stretching the curriculum over half the total epochs)
    curriculum_callback = ContextWindowCurriculum(
        collate_fn=collate_fn, 
        warmup_epochs=max_epochs // 2, 
        start_max_n=128, 
        end_max_n=4096,
    )

    trainer = pl.Trainer(
        max_epochs=max_epochs,
        accelerator="auto",
        devices="auto",
        strategy=DDPStrategy(find_unused_parameters=True),
        logger=logger,
        callbacks=[
            early_stop_callback, 
            model_checkpoint_callback, 
            curriculum_callback, # 4. Add it to the Trainer
        ],
        default_root_dir=logger.log_dir,
        # use bfloat16 precision for faster training and lower memory usage
        precision="bf16",
    )

    trainer.fit(model, dataloader)
    print(f"Phase {training_task} complete. Logs: {logger.log_dir}")

    return model_checkpoint_callback.best_model_path


if __name__ == "__main__":
    torch.autograd.graph.set_warn_on_accumulate_grad_stream_mismatch(False)
    torch.set_float32_matmul_precision('medium')
    pl.seed_everything(42)

    import sys

    try:
        smiles_file = sys.argv[1]
    except:
        print("Usage: python train.py /path/to/smiles.parquet")
        sys.exit(1)

    import polars

    smiles = polars.read_parquet(smiles_file)["SMILES"].to_list()

    from rdkit.rdBase import BlockLogs

    # shh!
    bl = BlockLogs()

    # Phase 1: Regression pre-training from scratch
    reg_ckpt = run_training(smiles, max_epochs=512, training_task="regression")

    # Phase 2: Classification pre-training from scratch
    cls_ckpt = run_training(smiles, max_epochs=512, training_task="classification")

    print(f"Both phases complete.")
    print(f"  Regression checkpoint: {reg_ckpt}")
    print(f"  Classification checkpoint: {cls_ckpt}")

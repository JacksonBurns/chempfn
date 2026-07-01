import torch
import lightning.pytorch as pl
from lightning.pytorch.callbacks import EarlyStopping
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
        return idx  # dummy — actual sampling happens in collate_fn

def make_collate_fn(X_full, min_n=16, max_n=512):
    def collate_fn(batch):
        B = len(batch)
        n_samples = torch.randint(min_n, max_n + 1, (1,)).item()
        idx = torch.randint(0, len(X_full), (B, n_samples))
        return X_full[idx]  # (B, n_samples, D), fully vectorized gather
    return collate_fn


def run_training(smiles_list, max_epochs=512):
    X_raw = get_rdkit_features(smiles_list)
    X_mean = torch.tensor(X_raw.mean(axis=0), dtype=torch.float32)
    X_std = torch.tensor(X_raw.std(axis=0) + 1e-6, dtype=torch.float32)
    X_normalized = (torch.tensor(X_raw) - X_mean) / X_std

    dataset = PFNSyntheticDataset(X_normalized)
    dataloader = DataLoader(
        dataset,
        batch_size=64,
        num_workers=0,
        shuffle=True,
        collate_fn=make_collate_fn(X_normalized),
    )

    model = ChemPFN(d_in=X_normalized.shape[1], max_classes=2)
    model.X_mean = X_mean
    model.X_std = X_std
    
    # 1. Setup TensorBoard Logger
    logger = TensorBoardLogger(save_dir="logs/", name="chem_pfn_experiment", default_hp_metric=False)

    # 2. Setup Early Stopping
    # Monitors 'train_loss'
    early_stop_callback = EarlyStopping(
        monitor="train_loss_epoch", 
        patience=10,
        mode="min"
    )

    # 3. Update Trainer
    trainer = pl.Trainer(
        max_epochs=max_epochs,
        accelerator="auto", 
        devices=1,
        default_root_dir="./pfn_checkpoints",
        logger=logger,
        callbacks=[early_stop_callback],
        gradient_clip_val=0.5,
    )
    
    trainer.fit(model, dataloader)
    print(f"Training complete. Logs available in: {logger.log_dir}")

if __name__ == "__main__":
    pl.seed_everything(42)
    with open("cleaned_pubchem_1MM.smiles", "r") as file:
        smiles = [line.strip() for line in file.readlines()]
    run_training(smiles)

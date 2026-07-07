# ChemPFN — Agent Instructions

## What this is

In-context learning chemistry model (PFN-style) built on a frozen CheMeleon molecule encoder. Flat single-file structure — no build system, no tests, no linter.

## File roles

| File | Purpose |
|---|---|
| `model.py` | Core `ChemPFN` LightningModule + frozen CheMeleon encoder + featurizer |
| `train.py` | Training loop: curriculum learning, data loading, callbacks |
| `inference.py` | `run_inference()` and `calibrate_threshold()` for downstream tasks |
| `eval.py` | Runs 28 Polaris/TDCommons benchmarks, writes `eval_results.md` |

## Commands

```
# Train both phases from scratch (long-running, ~512 epochs each)
python train.py

# Run inference from a checkpoint
python inference.py /path/to/model.ckpt

# Evaluate on 28 benchmarks (requires both ckpts)
python eval.py /path/to/reg_model.ckpt /path/to/cls_model.ckpt
```

## Architecture

- `ChemPFN` wraps a **frozen** CheMeleon BondMessagePassing encoder (auto-downloaded to `~/.chemprop/chemeleon_mp.pt`)
- Only the projection head, transformer encoder, and task heads are trained
- Uses `DDPStrategy(find_unused_parameters=True)` — the classification and regression heads are not always used
- Training uses **bf16-mixed** precision
- Two independent training tasks: `"regression"` and `"classification"` — separate checkpoints
- Training data: `cleaned_pubchem_1MM.smiles` (~1M SMILES)

## Training quirks

- **Curriculum learning**: context window grows from 128 to 1024 over first half of epochs
- **Delayed early stopping**: tracking disabled until epoch 256 (matches curriculum warmup)
- **Synthetic targets**: during pre-training, labels are fabricated from CheMeleon embeddings via random MLPs — no real property labels used
- `SmilesDataset` has `length=65536` but randomly samples SMILES per step (the `__getitem__` just returns an index)
- Gradient accumulation is done manually in `training_step` (10 passes per step)

## Evaluation quirks

- `eval.py` auto-selects regression vs classification checkpoint based on benchmark `TargetType`
- Classification tasks run `calibrate_threshold()` to optimize decision boundary on a held-out calibration split
- Results append to `eval_results.md` — re-running overwrites the file
- Benchmarks use `polaris-lib` for data loading and metric computation

## Dependencies

Flat `requirements.txt` — no lockfile, no virtualenv convention. Key deps: `torch`, `lightning`, `polaris-lib`, `chemprop`, `rdkit`, `scikit-learn`.

## Checkpoint format

- Saved to `logs/{task}/<run>/checkpoints/model-{epoch:02d}-{train_loss_epoch:.4f}`
- `model.hparams.training_task` determines which head is used — set before `load_from_checkpoint` if repurposing

## No tests, no linting

There is no test suite, no type checker, and no formatter configured. Any verification requires manual import/forward-pass checks.

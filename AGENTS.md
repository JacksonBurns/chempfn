# AGENTS.md

## Project Overview

ChemPFN — a TabPFN/TabICL-style transformer trained exclusively on chemistry data. Input features are always RDKit Morgan count fingerprints (2048) + continuous descriptors. Trained via synthetic priors (random MLP/tree targets) to learn in-context learning patterns, then applied at inference time with real context/test splits.

## Architecture

- `model.py` — ChemPFN LightningModule with transformer encoder, synthetic prior generation, SAM optimizer
- `train.py` — Training loop: loads PubChem SMILES, computes features, runs synthetic training
- `features.py` — RDKit descriptor + Morgan count fingerprint extraction with SQLite caching
- `inference.py` — In-context inference with sub-sampling ensemble, calibration utilities
- `eval.py` — Polaris benchmark evaluation pipeline
- `optim.py` — Sharpness-Aware Minimization (SAM) optimizer wrapper

## Key Design Decisions

- Fingerprints use `DenseCountEmbeddingBag` (matmul-based) instead of `nn.EmbeddingBag` for speed with cached dense count arrays
- Fingerprints are normalized with `log1p` before embedding to bring count magnitudes into descriptor range
- Learned positional encodings enable ICL context/query distinction
- `query_mask_token` is used for both regression and classification at query positions
- Attention mask excludes query positions from key attention (no cross-query leakage)
- SAM optimizer used for sharper generalization
- Synthetic priors simulate chemistry assay artifacts (LOD clipping, class imbalance)

## Commands

```bash
# Compute features (cached in .rdkit_feature_cache/)
python -c "from features import get_rdkit_features; ..."

# Train
python train.py

# Inference
python inference.py /path/to/model.ckpt

# Evaluate on Polaris benchmarks
python eval.py /path/to/model.ckpt
```

## Conventions

- All SMILES processing uses RDKit with multiprocessing + SQLite cache
- Model uses `batch_first=True` throughout
- Labels are zero-mean normalized during training and inference
- Classification uses softmax probabilities, not logits, at inference time
- Sign commits as "Qwen 3.6 27B via opencode"

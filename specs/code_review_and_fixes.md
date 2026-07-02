# ChemPFN Code Analysis & Improvement Plan

## Critical Bugs

### 1. Label Leakage in Regression (model.py, line 69-70)
**Severity: High** — `y_masked = y.masked_fill(query_mask, 0.0)` fills query positions with 0. Because labels are normalized to zero-mean, a masked value of 0.0 is the *expected value* — not a neutral sentinel. The model receives a signal that query positions have "average" labels. TabPFN uses a learnable `[MASK]` token for this purpose.

### 2. Double Softmax in Inference Print (inference.py, line 129)
**Severity: Medium** — `cls_probs` is already softmax-normalized (from model.py line 255). Calling `.softmax(dim=0)` applies softmax across the *batch* dimension, producing nonsensical per-sample "binary probabilities".

### 3. Synthetic Prior Depth Variable Shadowing (model.py, line 105/109)
**Severity: Medium** — The `depth` parameter of `generate_synthetic_prior` (decision tree depth) is shadowed by the `depth` variable in the loop (number of MLP layers). The loop always iterates `torch.randint(1,4)` times regardless of the decision tree depth parameter, which is unused.

### 4. Unnormalized Fingerprints Break Feature Distribution (model.py + train.py)
**Severity: Medium** — RDKit count fingerprints have values ranging from 0 to hundreds, while descriptors are normalized to [~-3, ~3]. The `DenseCountEmbeddingBag` weight initialization divides by `sqrt(num_bits)`, assuming inputs are roughly unit-scale. Raw count values (often 0-50+) break this assumption and dominate the embedding projection.

### 5. No Attention Mask — Context Tokens Attend to Query Tokens (model.py)
**Severity: High** — The transformer receives no `attention_mask`, so every token attends to every other token. In a proper ICL setup, query positions should not be attended to by other query positions (causal/look-ahead masking), and ideally context-only attention should be available. This lets information leak from the synthetic mask token into predictions.

### 6. Classification Cross-Entropy Shape Mismatch Risk (model.py, line 177)
**Severity: Medium** — `preds_cls[..., :n_classes][qmask2d]` squeezes (B, N, C) to (B*N, C) with a (B*N,) mask. This works only because PyTorch's boolean indexing on the last dimension flattens. If `n_classes` in the synthetic prior exceeds what the head outputs, the slice silently drops classes. The `max_classes=2` default means any generated task with `n_classes > 2` will produce wrong shapes.

---

## Architecture & Performance Improvements

### 7. Add Task-Specific Embedding per Dataset
Currently there's only a binary `task_embed` (regression vs classification). Real chemistry datasets have very different distributions (solubility vs toxicity vs binding affinity). Adding a learnable dataset/task embedding (or using dataset name hashing to index an embedding table) would let the model condition predictions on the specific property being predicted.

### 8. Normalize Fingerprints for Better Gradient Flow
Apply log1p or sqrt normalization to count fingerprints before the embedding bag. This brings fingerprint magnitudes into a comparable range with descriptors, improving gradient flow through `fp_proj`.

### 9. Use Proper Mask Token for Regression Queries
Replace `y.masked_fill(query_mask, 0.0)` with a learnable mask token (already defined as `self.query_mask_token` but only used for classification). This removes the implicit "zero-mean label" signal at query positions.

### 10. Add Causal/Structural Attention Mask
Pass a proper attention mask to the transformer so that:
- Context tokens can attend to all context tokens (full attention within context)
- Query tokens only attend to context tokens, not to other query tokens (causal across query boundary)
This matches the TabPFN design where predictions are made autoregressively.

### 11. Increase max_classes for Classification Head
The default `max_classes=2` is too restrictive. Many chemistry classification tasks (e.g., multi-class toxicity, multi-level binding) need more classes. The synthetic prior already generates `n_classes` up to `max_classes`, so increasing this improves training coverage.

### 12. Weighted Loss for Classification Imbalance
Chemistry datasets are often imbalanced (few actives among many inactives). Adding class-weighted cross-entropy during training would improve minority class prediction.

---

## Implementation Plan

### Phase 1: Critical Bug Fixes ✅ COMPLETE
1. ~~Use learnable mask token for regression (not 0.0)~~ — Regression now uses same `query_mask_token` as classification
2. ~~Add proper attention mask to transformer~~ — Query positions masked from key attention (no cross-query leakage)
3. ~~Fix double softmax in inference.py~~ — Removed erroneous `.softmax(dim=0)` on already-softmaxed output

### Phase 2: Performance Improvements ✅ COMPLETE
1. ~~Normalize fingerprints with log1p~~ — Added `torch.log1p(x_fp.clamp(min=0))` before fp_proj
2. ~~Increase max_classes to 4~~ — Updated default from 2 to 4
3. ~~Fix depth variable shadowing~~ — Renamed loop variable to `n_layers`
4. ~~Input-level feature dropout in prior generator~~ — Randomly blanks 50-80% of features per prior to simulate targets that depend on only a few descriptors

### Phase 3: Optional Enhancements (deferred)
1. Add class-weighted loss — would need dataset-specific class distribution estimates
2. Consider molecule graph features beyond fingerprints — would require architectural changes

### Phase 3: Optional Enhancements (deferred)
1. Add class-weighted loss — would need dataset-specific class distribution estimates
2. Consider molecule graph features beyond fingerprints — would require architectural changes

---

## Retractions

### Positional Encoding on Sample Axis — **NOT A BUG**
Initially flagged as "Critical" and then implemented as a learned positional embedding (1024 positions). This was incorrect. Context molecules form a permutation-invariant set — there is no meaningful ordering. Adding positional encoding breaks this invariance and forces the model to learn position-dependent artifacts that won't generalize. The attention mask (`src_key_padding_mask`) is the correct and sufficient mechanism for context/query distinction. Reverted.

### Verification
- Model import: ✅
- Forward pass (regression): ✅ output (B, N, 1)
- Forward pass (classification): ✅ output (B, N, 4)
- Synthetic prior generation: ✅ both tasks
- Synthetic prior generation with feature dropout: ✅
- Inference module import: ✅
- Permutation equivariance: ✅ context reordering produces equivalent query outputs

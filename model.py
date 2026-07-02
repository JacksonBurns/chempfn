import torch
import torch.nn as nn
import torch.nn.functional as F
import lightning.pytorch as pl
import math
from features import get_rdkit_features
from optim import SAM

class DenseCountEmbeddingBag(nn.Module):
    """
    A dense implementation mathematically equivalent to nn.EmbeddingBag(mode='sum').
    Since the caching system outputs dense multi-hot/count arrays, using
    matmul is significantly faster than converting to sparse indices/offsets on the fly.
    """
    def __init__(self, num_bits, d_model):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(num_bits, d_model) / math.sqrt(num_bits))

    def forward(self, counts):
        # counts: (..., num_bits), weight: (num_bits, d_model)
        return torch.matmul(counts, self.weight)

class ChemPFN(pl.LightningModule):
    def __init__(self, d_desc, d_fp=2048, d_model=512, n_heads=4, n_layers=8, lr=1e-4,
                 hidden_dim=256, max_classes=4):
        super().__init__()
        self.save_hyperparameters()

        # REQUIRED FOR SAM: Turn off Lightning's automatic step calls
        self.automatic_optimization = False

        # We track mean/std for the combined feature vector so predict_step can remain untouched
        self.register_buffer("X_mean", torch.zeros(d_desc + d_fp))
        self.register_buffer("X_std", torch.ones(d_desc + d_fp))

        # Separate projections for continuous descriptors vs discrete counts
        self.desc_proj = nn.Linear(d_desc, d_model)
        self.fp_proj = DenseCountEmbeddingBag(d_fp, d_model)

        self.y_proj_reg = nn.Linear(1, d_model)
        self.y_embed_cls = nn.Embedding(max_classes, d_model)
        self.query_mask_token = nn.Parameter(torch.randn(d_model) * 0.02)
        self.task_embed = nn.Embedding(2, d_model)  # 0=regression, 1=classification

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=n_heads, dim_feedforward=d_model * 4,
            batch_first=True, norm_first=True, activation="gelu"
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=n_layers)
        self.head_reg = nn.Linear(d_model, 1)
        self.head_cls = nn.Linear(d_model, max_classes)

    def forward(self, x, y, query_mask, task="regression"):
        d_desc = self.hparams.d_desc

        # Split the raw input tensor
        x_desc = x[..., :d_desc]
        x_fp = x[..., d_desc:]

        # Normalize count fingerprints (log1p brings sparse counts to manageable range)
        x_fp = torch.log1p(x_fp.clamp(min=0))

        # Project and sum
        desc_tok = self.desc_proj(x_desc)
        fp_tok = self.fp_proj(x_fp)
        x_tok = desc_tok + fp_tok

        task_idx = torch.tensor(0 if task == "regression" else 1, device=x.device)
        task_tok = self.task_embed(task_idx).view(1, 1, -1)

        if task == "regression":
            y_tok = self.y_proj_reg(y)
            mask_tok = self.query_mask_token.view(1, 1, -1).expand_as(y_tok)
            y_tok = torch.where(query_mask, mask_tok, y_tok)
        else:
            y_tok = self.y_embed_cls(y.clamp(min=0))
            mask_tok = self.query_mask_token.view(1, 1, -1).expand_as(y_tok)
            y_tok = torch.where(query_mask, mask_tok, y_tok)

        tokens = x_tok + y_tok + task_tok

        # Attention mask: mask out query positions from key attention
        # src_key_padding_mask is (B, N) where True = don't attend to this key position
        q = query_mask.squeeze(-1)  # (B, N)
        out = self.transformer(tokens, src_key_padding_mask=q)
        return self.head_reg(out) if task == "regression" else self.head_cls(out)

    def _random_mlp_layer(self, h, in_dim, H, act, device):
        B = h.shape[0]
        W = torch.randn(B, in_dim, H, device=device) / math.sqrt(in_dim)
        b = torch.randn(B, 1, H, device=device) * 0.1
        return act(torch.bmm(h, W) + b)

    def _random_tree_layer(self, h, H, device, depth=3, n_trees=4):
        B, N, in_dim = h.shape
        n_leaves = 2 ** depth
        out = torch.zeros(B, N, H, device=device)
        powers = (2 ** torch.arange(depth, device=device)).view(1, 1, depth)
        for _ in range(n_trees):
            feat_idx = torch.randint(0, in_dim, (B, depth), device=device)
            feat_vals = torch.gather(h, 2, feat_idx.unsqueeze(1).expand(B, N, depth))
            thresholds = torch.randn(B, 1, depth, device=device) * 0.5
            bits = (feat_vals > thresholds).long()
            leaf_idx = (bits * powers).sum(-1)
            leaf_values = torch.randn(B, n_leaves, H, device=device) / math.sqrt(depth + 1)
            out = out + torch.gather(leaf_values, 1, leaf_idx.unsqueeze(-1).expand(B, N, H))
        return out / n_trees

    def generate_synthetic_prior(self, x, task):
        B, N, D = x.shape
        H = self.hparams.hidden_dim
        device = self.device
        n_layers = torch.randint(1, 4, (1,)).item()
        activations = [F.relu, torch.tanh, F.gelu]

        # Feature dropout: blank out 50-80% of features per prior to simulate
        # chemistry targets that depend on only a few descriptors/fingerprint bits
        dropout_rate = torch.empty(1, device=device).uniform_(0.5, 0.8).item()
        keep_mask = torch.rand(B, 1, D, device=device) > dropout_rate
        h = x * keep_mask
        in_dim = D

        for _ in range(n_layers):
            if torch.rand(1).item() > 0.5:
                act = activations[torch.randint(0, len(activations), (1,)).item()]
                h = self._random_mlp_layer(h, in_dim, H, act, device)
            else:
                h = self._random_tree_layer(h, H, device)
            in_dim = H

        W_out = torch.randn(B, in_dim, 1, device=device) / math.sqrt(in_dim)
        raw = torch.bmm(h, W_out)
        raw = raw + torch.randn_like(raw) * (torch.rand(B, 1, 1, device=device) * 0.1)

        if task == "regression":
            targets = (raw - raw.mean(1, keepdim=True)) / (raw.std(1, keepdim=True) + 1e-6)

            # --- CHEMINFORMATICS REALITY: Zero-Inflated / Clipped Assays ---
            # 50% chance to simulate a lower limit of detection (LOD)
            if torch.rand(1).item() > 0.5:
                q_floor = torch.rand(1, device=device).item() * 0.25 # Clip bottom 0-25%
                floor_val = torch.quantile(targets, q_floor, dim=1, keepdim=True)
                targets = torch.max(targets, floor_val)

            # 25% chance to also simulate an upper assay saturation point
            if torch.rand(1).item() > 0.75:
                q_ceil = 1.0 - (torch.rand(1, device=device).item() * 0.25)
                ceil_val = torch.quantile(targets, q_ceil, dim=1, keepdim=True)
                targets = torch.min(targets, ceil_val)

            return targets

        n_classes = torch.randint(2, self.hparams.max_classes + 1, (1,)).item()

        # --- CHEMINFORMATICS REALITY: Extreme Class Imbalance ---
        if n_classes == 2:
            # Random active class ratio between 1% and 50%
            pos_ratio = torch.empty(1, device=device).uniform_(0.01, 0.5).item()
            qs = torch.tensor([1.0 - pos_ratio], device=device)
        else:
            # For multi-class, randomly skew bucket sizes instead of linspace
            qs = torch.rand(n_classes - 1, device=device).sort()[0]

        edges = torch.quantile(raw.squeeze(-1), qs, dim=1).transpose(0, 1)
        labels = torch.zeros(B, N, dtype=torch.long, device=device)
        for c in range(n_classes - 1):
            labels += (raw.squeeze(-1) > edges[:, c:c + 1]).long()

        return labels, n_classes

    def training_step(self, batch, batch_idx):
        x_batch = batch
        B, N, _ = x_batch.shape
        query_mask = torch.rand(B, N, 1, device=self.device) > 0.5

        # 1. Generate BOTH synthetic datasets for this batch of X
        y_reg = self.generate_synthetic_prior(x_batch, task="regression")
        y_cls, n_classes = self.generate_synthetic_prior(x_batch, task="classification")
        qmask2d = query_mask.squeeze(-1)

        opt = self.optimizers()

        # 2. Define a joint loss computation
        def compute_loss():
            # Forward pass 1: Regression
            preds_reg = self(x_batch, y_reg, query_mask, task="regression")
            loss_reg = F.mse_loss(preds_reg[query_mask], y_reg[query_mask])
            
            # Forward pass 2: Classification
            preds_cls = self(x_batch, y_cls, query_mask, task="classification")
            loss_cls = F.cross_entropy(preds_cls[..., :n_classes][qmask2d], y_cls[qmask2d])
            
            # Sum the losses so gradients flow to all heads and projection layers
            total_loss = loss_reg + loss_cls
            return total_loss, loss_reg, loss_cls

        # --- SAM Pass 1: Climb to the sharpest point in the joint neighborhood ---
        total_loss, loss_reg, loss_cls = compute_loss()
        self.manual_backward(total_loss)
        opt.first_step(zero_grad=True)

        # --- SAM Pass 2: Calculate gradients at the sharp point to update weights ---
        total_loss_2, _, _ = compute_loss()
        self.manual_backward(total_loss_2)
        opt.step(zero_grad=True)

        # 3. Comprehensive Logging
        self.log("train_loss", total_loss, prog_bar=True, on_step=True, on_epoch=True, sync_dist=True)
        self.log("train_loss_regression", loss_reg, on_step=True, on_epoch=True, sync_dist=True)
        self.log("train_loss_classification", loss_cls, on_step=True, on_epoch=True, sync_dist=True)
        
        # Log the sharpness penalty (how much worse the joint loss gets after the SAM step)
        self.log("train_loss_sam_penalty", total_loss_2 - total_loss, on_step=True, on_epoch=True, sync_dist=True)

        return total_loss.detach()

    def predict_step(self, batch, batch_idx, dataloader_idx=0, task="regression",
                  n_classes=None, max_context=512, n_ensemble=4):
        train_smiles, train_labels, test_smiles = batch
        
        if task == "regression":
            labels_raw = torch.tensor(train_labels, dtype=torch.float32, device=self.device)
            y_mean, y_std = labels_raw.mean(), labels_raw.std() + 1e-6
            labels_proc = (labels_raw - y_mean) / y_std
        else:
            assert n_classes is not None, "pass n_classes for classification"
            labels_proc = torch.tensor(train_labels, dtype=torch.long, device=self.device)

        all_smiles = list(train_smiles) + list(test_smiles)
        X_raw = torch.tensor(get_rdkit_features(all_smiles), dtype=torch.float32, device=self.device)
        
        # This will correctly normalize ONLY the descriptors since the FP part of X_mean is 0
        X = (X_raw - self.X_mean) / self.X_std

        n_train = len(train_labels)
        X_train, X_test = X[:n_train], X[n_train:]
        n_test = X_test.shape[0]
        test_budget = max(max_context - min(n_train, max_context), 1)
        out_dim = 1 if task == "regression" else n_classes
        preds_sum = torch.zeros(n_test, out_dim, device=self.device)

        for chunk_start in range(0, n_test, test_budget):
            chunk_end = min(chunk_start + test_budget, n_test)
            X_chunk = X_test[chunk_start:chunk_end]
            chunk_size = X_chunk.shape[0]
            passes = n_ensemble if n_train > max_context - chunk_size else 1
            chunk_preds = torch.zeros(chunk_size, out_dim, device=self.device)

            for _ in range(passes):
                if n_train > max_context - chunk_size:
                    ctx_n = max_context - chunk_size
                    idx = torch.randperm(n_train, device=self.device)[:ctx_n]
                else:
                    idx = torch.arange(n_train, device=self.device)

                X_combined = torch.cat([X_train[idx], X_chunk], dim=0).unsqueeze(0)
                total_len = X_combined.shape[1]
                mask = torch.zeros(1, total_len, 1, dtype=torch.bool, device=self.device)
                mask[0, len(idx):, 0] = True

                if task == "regression":
                    y_combined = torch.zeros(1, total_len, 1, device=self.device)
                    y_combined[0, :len(idx), 0] = labels_proc[idx]
                    out = self(X_combined, y_combined, mask, task="regression")[mask].view(-1, 1)
                else:
                    y_combined = torch.zeros(1, total_len, dtype=torch.long, device=self.device)
                    y_combined[0, :len(idx)] = labels_proc[idx]
                    logits = self(X_combined, y_combined, mask, task="classification")[0, len(idx):, :n_classes]
                    out = F.softmax(logits, dim=-1)
                
                chunk_preds += out
                
            preds_sum[chunk_start:chunk_end] = chunk_preds / passes
            
        if task == "regression":
            return preds_sum * y_std + y_mean
            
        return preds_sum 
    
    def configure_optimizers(self):
        # Wrap AdamW inside our SAM optimizer
        base_opt = torch.optim.AdamW
        # rho=0.05 is the standard SAM neighborhood size
        return SAM(self.parameters(), base_opt, lr=self.hparams.lr, rho=0.05)

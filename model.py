import torch
import torch.nn as nn
import torch.nn.functional as F
import lightning.pytorch as pl
import math
from features import get_rdkit_features

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
    def __init__(self, d_desc, d_fp=2048, d_model=512, n_heads=8, n_layers=8, lr=1e-4,
                 hidden_dim=128, max_classes=10):
        super().__init__()
        self.save_hyperparameters()

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

        # Project and sum
        desc_tok = self.desc_proj(x_desc)
        fp_tok = self.fp_proj(x_fp)
        x_tok = desc_tok + fp_tok

        task_idx = torch.tensor(0 if task == "regression" else 1, device=x.device)
        task_tok = self.task_embed(task_idx).view(1, 1, -1)

        if task == "regression":
            y_masked = y.masked_fill(query_mask, 0.0)
            y_tok = self.y_proj_reg(y_masked)
        else:
            y_tok = self.y_embed_cls(y.clamp(min=0))
            mask_tok = self.query_mask_token.view(1, 1, -1).expand_as(y_tok)
            y_tok = torch.where(query_mask, mask_tok, y_tok)

        tokens = x_tok + y_tok + task_tok
        out = self.transformer(tokens)
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
        depth = torch.randint(1, 4, (1,)).item()
        activations = [F.relu, torch.tanh, F.gelu]
        h, in_dim = x, D

        for _ in range(depth):
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
            return targets  
            
        n_classes = torch.randint(2, self.hparams.max_classes + 1, (1,)).item()
        qs = torch.linspace(0, 1, n_classes + 1, device=device)[1:-1]
        edges = torch.quantile(raw.squeeze(-1), qs, dim=1).transpose(0, 1)  
        labels = torch.zeros(B, N, dtype=torch.long, device=device)
        for c in range(n_classes - 1):
            labels += (raw.squeeze(-1) > edges[:, c:c + 1]).long()
        return labels, n_classes  

    def training_step(self, batch, batch_idx):
        x_batch = batch
        B, N, _ = x_batch.shape
        task = "classification" if torch.rand(1).item() > 0.5 else "regression"
        query_mask = torch.rand(B, N, 1, device=self.device) > 0.5

        if task == "regression":
            y_batch = self.generate_synthetic_prior(x_batch, task="regression")
            preds = self(x_batch, y_batch, query_mask, task="regression")
            loss = F.mse_loss(preds[query_mask], y_batch[query_mask])
        else:
            y_batch, n_classes = self.generate_synthetic_prior(x_batch, task="classification")
            qmask2d = query_mask.squeeze(-1)
            preds = self(x_batch, y_batch, query_mask, task="classification")
            loss = F.cross_entropy(preds[..., :n_classes][qmask2d], y_batch[qmask2d])

        self.log("train_loss", loss, prog_bar=True, on_step=True, on_epoch=True)
        self.log(f"train_loss_{task}", loss, on_step=True, on_epoch=True)
        return loss

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
        return torch.optim.AdamW(self.parameters(), lr=self.hparams.lr)

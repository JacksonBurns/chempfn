import math
from pathlib import Path
from urllib.request import urlretrieve

import torch
import torch.nn as nn
import torch.nn.functional as F
import lightning.pytorch as pl
from chemprop import nn as cp_nn

from chemprop.featurizers import CuikmolmakerMolGraphFeaturizer

featurizer = CuikmolmakerMolGraphFeaturizer()


def _move_graph_to(graph, device):
    """Move BatchCuikMolGraph fields to device."""
    for field in ("V", "E", "edge_index", "rev_edge_index", "batch"):
        v = getattr(graph, field, None)
        if v is not None:
            setattr(graph, field, v.to(device))
    return graph


def _random_mlp_hyperdescriptor(y_subset, H, device):
    """Create a scalar hyperdescriptor from a subset of descriptors via a random MLP."""
    B, N, K = y_subset.shape
    depth = torch.randint(0, 3, (1,)).item()

    if depth == 0:
        W = torch.randn(B, K, 1, device=device) / math.sqrt(K)
        out = torch.bmm(y_subset, W)
    elif depth == 1:
        W1 = torch.randn(B, K, H, device=device) / math.sqrt(K)
        b1 = torch.randn(B, 1, H, device=device) * 0.1
        h = torch.relu(torch.bmm(y_subset, W1) + b1)
        W2 = torch.randn(B, H, 1, device=device) / math.sqrt(H)
        b2 = torch.randn(B, 1, 1, device=device) * 0.1
        out = torch.bmm(h, W2) + b2
    else:
        W1 = torch.randn(B, K, H, device=device) / math.sqrt(K)
        b1 = torch.randn(B, 1, H, device=device) * 0.1
        h = torch.relu(torch.bmm(y_subset, W1) + b1)
        W2 = torch.randn(B, H, H, device=device) / math.sqrt(H)
        b2 = torch.randn(B, 1, H, device=device) * 0.1
        h = torch.relu(torch.bmm(h, W2) + b2)
        W3 = torch.randn(B, H, 1, device=device) / math.sqrt(H)
        b3 = torch.randn(B, 1, 1, device=device) * 0.1
        out = torch.bmm(h, W3) + b3

    out = (out - out.mean(dim=1, keepdim=True)) / (out.std(dim=1, keepdim=True) + 1e-6)
    return out


class ChemPFN(pl.LightningModule):
    def __init__(self, d_model=512, n_heads=4, n_layers=8, lr=1e-4,
                 max_classes=4, training_task="regression", d_task=32):
        super().__init__()
        self.save_hyperparameters()

        # Initialize and freeze the CheMeleon foundation model
        ckpt_dir = Path().home() / ".chemprop"
        ckpt_dir.mkdir(exist_ok=True)
        mp_path = ckpt_dir / "chemeleon_mp.pt"
        if not mp_path.exists():
            urlretrieve(
                r"https://zenodo.org/records/15460715/files/chemeleon_mp.pt",
                mp_path,
            )
        chemeleon_mp = torch.load(mp_path, weights_only=True)
        self.chemeleon_encoder = cp_nn.BondMessagePassing(**chemeleon_mp["hyper_parameters"])
        self.chemeleon_encoder.load_state_dict(chemeleon_mp["state_dict"])
        self.chemeleon_agg = cp_nn.MeanAggregation()

        assert d_model > 256, "d_model must be greater than 256 to accommodate projection head and regression/classification head"

        for param in self.chemeleon_encoder.parameters():
            param.requires_grad = False

        # Projection head to reduce to d_model - d_task
        self.x_proj = nn.Linear(self.chemeleon_encoder.output_dim, d_model - d_task)

        # Regression: single scalar label projection
        self.y_proj_reg = nn.Linear(1, d_task)
        # Head takes the fully concatenated output from the transformer (d_model)
        self.head_reg = nn.Linear(d_model, 1)

        # Classification: class embedding
        self.y_embed_cls = nn.Embedding(max_classes, d_task)
        # Head takes the fully concatenated output from the transformer (d_model)
        self.head_cls = nn.Linear(d_model, max_classes)

        # Use nn.Embedding so it registers as a distinct module in the PyTorch Lightning summary
        self.query_mask_token = nn.Embedding(1, d_task)
        nn.init.normal_(self.query_mask_token.weight, mean=0.0, std=0.02)

        # Transformer expects exactly d_model
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=n_heads, dim_feedforward=d_model * 4,
            batch_first=True, norm_first=True, activation="gelu",
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=n_layers)

    def forward(self, x, y, query_mask, task="regression"):
        if not isinstance(x, torch.Tensor):
            with torch.no_grad():
                self.chemeleon_encoder.eval()
                x_chemeleon = self.chemeleon_agg(self.chemeleon_encoder(x), x.batch)
            x_chemeleon = x_chemeleon.view(1, -1, self.chemeleon_encoder.output_dim)
        else:
            x_chemeleon = x

        x_tok = self.x_proj(x_chemeleon)

        if task == "regression":
            y_tok = self.y_proj_reg(y)
        else:
            y_tok = self.y_embed_cls(y.clamp(min=0))

        mask_tok = self.query_mask_token.weight.view(1, 1, -1).expand_as(y_tok)
        y_tok = torch.where(query_mask, mask_tok, y_tok)

        tokens = torch.cat([x_tok, y_tok], dim=-1)
        q = query_mask.squeeze(-1)
        
        out = self.transformer(tokens, src_key_padding_mask=q)

        if task == "regression":
            return self.head_reg(out)
        return self.head_cls(out)

    def training_step(self, batch, batch_idx):
        graph = batch[0]
        graph = _move_graph_to(graph, self.device)

        with torch.no_grad():
            self.chemeleon_encoder.eval()
            x_chemeleon = self.chemeleon_agg(self.chemeleon_encoder(graph), graph.batch)
        x_chemeleon = x_chemeleon.view(1, -1, self.chemeleon_encoder.output_dim)

        B, N, D = 1, x_chemeleon.shape[1], x_chemeleon.shape[2]
        
        # Dynamic Masking Ratio (10% to 90%)
        # This decouples the model from a fixed 1:1 context/query split
        mask_prob = torch.rand(1, device=self.device).item() * 0.8 + 0.1
        query_mask = torch.rand(B, N, 1, device=self.device) > mask_prob

        n_accum = 10
        H = 32
        
        K = torch.randint(max(5, D // 20), max(10, D // 2), (1,)).item()
        k_idx = torch.randperm(D, device=self.device)[:K]
        y_subset = x_chemeleon[:, :, k_idx]

        task = self.hparams.training_task

        if task == "regression":
            loss = 0.0
            for _ in range(n_accum):
                y_hyper = _random_mlp_hyperdescriptor(y_subset, H, self.device)
                preds = self(x_chemeleon, y_hyper, query_mask, task="regression")
                q = query_mask.squeeze(-1)
                loss += F.mse_loss(preds[q], y_hyper[q])
            loss /= n_accum
        else:
            loss = 0.0
            for _ in range(n_accum):
                y_hyper = _random_mlp_hyperdescriptor(y_subset, H, self.device)
                q = query_mask.squeeze(-1)
                context_vals = y_hyper[~q, 0]
                median = context_vals.median() if context_vals.numel() > 1 else context_vals.mean()
                y_cls = (y_hyper[:, :, 0] >= median).long()
                preds = self(x_chemeleon, y_cls, query_mask, task="classification")
                loss += F.cross_entropy(preds[..., :2][q], y_cls[q])
            loss /= n_accum

        self.log("train_loss", loss, prog_bar=True, on_step=True, on_epoch=True, sync_dist=True, batch_size=N)
        return loss

    def predict_step(self, batch, batch_idx, dataloader_idx=0, task="regression",
                     n_classes=None, max_context=512, n_ensemble=4):
        train_smiles, train_labels, test_smiles = batch

        if task == "regression":
            labels_raw = torch.tensor(train_labels, dtype=torch.float32, device=self.device)
            y_mean = labels_raw.mean()
            # Added unbiased=False to prevent NaN standard deviation on 1-shot inputs
            y_std = labels_raw.std(unbiased=False) + 1e-6
            labels_proc = ((labels_raw - y_mean) / y_std).unsqueeze(-1)
        else:
            assert n_classes is not None, "pass n_classes for classification"
            labels_proc = torch.tensor(train_labels, dtype=torch.long, device=self.device)

        all_smiles = list(train_smiles) + list(test_smiles)
        graph = featurizer(all_smiles)
        graph = _move_graph_to(graph, self.device)

        with torch.no_grad():
            self.chemeleon_encoder.eval()
            all_chemeleon = self.chemeleon_agg(self.chemeleon_encoder(graph), graph.batch).view(1, -1, self.chemeleon_encoder.output_dim)

        n_train = len(train_labels)
        n_test = len(test_smiles)
        train_x, test_x = all_chemeleon[:, :n_train], all_chemeleon[:, n_train:]
        
        # Ensure we always reserve space for test queries to maintain GPU throughput
        min_test_budget = min(512, n_test, max(1, max_context // 4))
        
        # Maximize context while leaving room for the guaranteed test budget
        ctx_n = min(n_train, max_context - min_test_budget)
        test_budget = max_context - ctx_n 
        
        out_dim = 1 if task == "regression" else n_classes
        preds_sum = torch.zeros(n_test, out_dim, device=self.device)

        for chunk_start in range(0, n_test, test_budget):
            chunk_end = min(chunk_start + test_budget, n_test)
            X_chunk = test_x[:, chunk_start:chunk_end]
            chunk_size = X_chunk.shape[1]
            passes = n_ensemble if n_train > ctx_n else 1
            chunk_preds = torch.zeros(chunk_size, out_dim, device=self.device)

            for _ in range(passes):
                if n_train > ctx_n:
                    # Cosine Similarity Context Retrieval (Fast MMD Proxy)
                    # Get the centroid of the current test chunk
                    chunk_mean = X_chunk.squeeze(0).mean(dim=0, keepdim=True) # [1, D]
                    train_flat = train_x.squeeze(0) # [n_train, D]
                    
                    # Compute similarity and retrieve the top-K matching contexts
                    sim = F.cosine_similarity(train_flat, chunk_mean, dim=-1)
                    _, idx = torch.topk(sim, ctx_n)
                else:
                    idx = torch.arange(n_train, device=self.device)

                X_combined = torch.cat([train_x[:, idx], X_chunk], dim=1)
                total_len = X_combined.shape[1]
                mask = torch.zeros(1, total_len, 1, dtype=torch.bool, device=self.device)
                mask[0, len(idx):, 0] = True

                if task == "regression":
                    y_combined = torch.zeros(1, total_len, 1, device=self.device)
                    y_combined[0, :len(idx), 0] = labels_proc[idx].squeeze(-1)
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
        return torch.optim.AdamW(filter(lambda p: p.requires_grad, self.parameters()), lr=self.hparams.lr)

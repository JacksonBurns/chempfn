import math
import torch
import torch.nn as nn
import torch.nn.functional as F
import lightning.pytorch as pl
from chemprop.featurizers import BatchCuikMolGraph
from chemprop.nn.message_passing import BondMessagePassing
from chemprop.nn import NormAggregation
from features import ATOM_FDIM, BOND_FDIM, N_DESC, get_featurizer, FEATURIZER

featurizer = get_featurizer(FEATURIZER)


def _move_graph_to(graph, device):
    """Move BatchCuikMolGraph fields to device."""
    for field in ("V", "E", "edge_index", "rev_edge_index", "batch"):
        v = getattr(graph, field, None)
        if v is not None:
            setattr(graph, field, v.to(device))
    return graph


def _random_mlp_hyperdescriptor(y_subset, H, device):
    """Create a scalar hyperdescriptor from a subset of descriptors via a random MLP.

    Randomly chooses depth in {0, 1, 2}:
      0: linear (K → 1)
      1: one hidden (K → H → 1)
      2: two hidden (K → H → H → 1)

    y_subset: (1, N, K) — selected descriptor columns
    Returns: (1, N, 1) zero-mean, unit-var scalar
    """
    B, N, K = y_subset.shape
    depth = torch.randint(0, 3, (1,)).item()

    if depth == 0:
        W = torch.randn(B, K, 1, device=device) / math.sqrt(K)
        out = torch.bmm(y_subset, W)
    elif depth == 1:
        W1 = torch.randn(B, K, H, device=device) / math.sqrt(K)
        b1 = torch.randn(B, 1, H, device=device) * 0.1
        h = torch.tanh(torch.bmm(y_subset, W1) + b1)
        W2 = torch.randn(B, H, 1, device=device) / math.sqrt(H)
        b2 = torch.randn(B, 1, 1, device=device) * 0.1
        out = torch.bmm(h, W2) + b2
    else:
        W1 = torch.randn(B, K, H, device=device) / math.sqrt(K)
        b1 = torch.randn(B, 1, H, device=device) * 0.1
        h = torch.tanh(torch.bmm(y_subset, W1) + b1)
        W2 = torch.randn(B, H, H, device=device) / math.sqrt(H)
        b2 = torch.randn(B, 1, H, device=device) * 0.1
        h = torch.tanh(torch.bmm(h, W2) + b2)
        W3 = torch.randn(B, H, 1, device=device) / math.sqrt(H)
        b3 = torch.randn(B, 1, 1, device=device) * 0.1
        out = torch.bmm(h, W3) + b3

    out = (out - out.mean(dim=1, keepdim=True)) / (out.std(dim=1, keepdim=True) + 1e-6)
    return out


class ChemPFN(pl.LightningModule):
    def __init__(self, d_model=512, n_heads=4, n_layers=8, lr=1e-4,
                 gnn_depth=6, max_classes=4, training_task="regression"):
        super().__init__()
        self.save_hyperparameters()

        # Learned GNN: atom/bond → molecular embedding
        self.gnn = BondMessagePassing(
            d_v=ATOM_FDIM, d_e=BOND_FDIM, d_h=d_model,
            depth=gnn_depth, activation="leakyrelu",
        )
        self.aggregator = NormAggregation()

        # Regression: single scalar label projection + head
        self.y_proj_reg = nn.Linear(1, d_model)
        self.head_reg = nn.Linear(d_model, 1)

        # Classification: class embedding + head
        self.y_embed_cls = nn.Embedding(max_classes, d_model)
        self.head_cls = nn.Linear(d_model, max_classes)

        self.query_mask_token = nn.Parameter(torch.randn(d_model) * 0.02)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=n_heads, dim_feedforward=d_model * 4,
            batch_first=True, norm_first=True, activation="gelu",
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=n_layers)

    def forward(self, x, y, query_mask, task="regression"):
        d_model = self.hparams.d_model

        if isinstance(x, BatchCuikMolGraph):
            n_mol = len(x.batch.unique())
            x_tok = self.aggregator(self.gnn(x), x.batch).view(1, n_mol, d_model)
        else:
            x_tok = x

        if task == "regression":
            y_tok = self.y_proj_reg(y)
        else:
            y_tok = self.y_embed_cls(y.clamp(min=0))

        mask_tok = self.query_mask_token.view(1, 1, -1).expand_as(y_tok)
        y_tok = torch.where(query_mask, mask_tok, y_tok)

        tokens = x_tok + y_tok
        q = query_mask.squeeze(-1)
        out = self.transformer(tokens, src_key_padding_mask=q)

        if task == "regression":
            return self.head_reg(out)
        return self.head_cls(out)

    def training_step(self, batch, batch_idx):
        graph, y = batch
        graph = _move_graph_to(graph, self.device)
        y = y.to(self.device).unsqueeze(0)  # (1, N, N_DESC)

        B, N, D = 1, y.shape[1], y.shape[2]
        query_mask = torch.rand(B, N, 1, device=self.device) > 0.5

        # Average over multiple random hyperdescriptors to reduce variance
        n_accum = 4
        H = 32
        K = torch.randint(max(5, D // 20), max(10, D // 2), (1,)).item()
        k_idx = torch.randperm(D, device=self.device)[:K]
        y_subset = y[:, :, k_idx]  # (1, N, K)

        task = self.hparams.training_task

        if task == "regression":
            loss = 0.0
            for _ in range(n_accum):
                y_hyper = _random_mlp_hyperdescriptor(y_subset, H, self.device)
                preds = self(graph, y_hyper, query_mask, task="regression")
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
                preds = self(graph, y_cls, query_mask, task="classification")
                loss += F.cross_entropy(preds[..., :2][q], y_cls[q])
            loss /= n_accum

        self.log("train_loss", loss, prog_bar=True, on_step=True, on_epoch=True, sync_dist=True, batch_size=N)
        return loss

    def predict_step(self, batch, batch_idx, dataloader_idx=0, task="regression",
                     n_classes=None, max_context=512, n_ensemble=4):
        train_smiles, train_labels, test_smiles = batch

        if task == "regression":
            labels_raw = torch.tensor(train_labels, dtype=torch.float32, device=self.device)
            y_mean, y_std = labels_raw.mean(), labels_raw.std() + 1e-6
            labels_proc = ((labels_raw - y_mean) / y_std).unsqueeze(-1)
        else:
            assert n_classes is not None, "pass n_classes for classification"
            labels_proc = torch.tensor(train_labels, dtype=torch.long, device=self.device)

        all_smiles = list(train_smiles) + list(test_smiles)
        graph = featurizer(all_smiles)
        graph = _move_graph_to(graph, self.device)

        d_model = self.hparams.d_model
        all_x = self.aggregator(self.gnn(graph), graph.batch).view(1, -1, d_model)

        n_train = len(train_labels)
        n_test = len(test_smiles)
        train_x, test_x = all_x[:, :n_train], all_x[:, n_train:]
        test_budget = max(max_context - min(n_train, max_context), 1)
        out_dim = 1 if task == "regression" else n_classes
        preds_sum = torch.zeros(n_test, out_dim, device=self.device)

        for chunk_start in range(0, n_test, test_budget):
            chunk_end = min(chunk_start + test_budget, n_test)
            X_chunk = test_x[:, chunk_start:chunk_end]
            chunk_size = X_chunk.shape[1]
            passes = n_ensemble if n_train > max_context - chunk_size else 1
            chunk_preds = torch.zeros(chunk_size, out_dim, device=self.device)

            for _ in range(passes):
                if n_train > max_context - chunk_size:
                    ctx_n = max_context - chunk_size
                    idx = torch.randperm(n_train, device=self.device)[:ctx_n]
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
        return torch.optim.AdamW(self.parameters(), lr=self.hparams.lr)

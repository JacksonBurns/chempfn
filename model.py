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

def _generate_synthetic_targets(y_subset, H, device):
    # IMMEDIATELY cast to float32 to prevent bfloat16 catastrophic cancellation in std()
    x_input = y_subset.float()
    B, N, K = x_input.shape
    
    # --- 1. SIMULATE REAL-WORLD ARTIFACTS ---
    if torch.rand(1).item() < 0.7:
        dropout_rate = torch.empty(1, device=device).uniform_(0.05, 0.30).item()
        dropout_mask = (torch.rand_like(x_input) > dropout_rate).float()
        x_input = x_input * dropout_mask
        
    prior_type = torch.rand(1).item()
    out = torch.zeros(B, N, 1, device=device, dtype=torch.float32)
    
    if prior_type < 0.33:
        # BNN Prior
        depth = torch.randint(1, 4, (1,)).item()
        h = x_input
        for _ in range(depth):
            weight_var = torch.empty(1, device=device).uniform_(0.1, 2.0).item()
            W = (torch.randn(B, h.shape[2], H, device=device) * math.sqrt(weight_var)) / math.sqrt(h.shape[2])
            b = torch.randn(B, 1, H, device=device) * 0.1
            
            act_choice = torch.rand(1).item()
            if act_choice < 0.33: act_fn = torch.relu
            elif act_choice < 0.66: act_fn = torch.tanh
            else: act_fn = torch.sin
            h = act_fn(torch.bmm(h, W) + b)
            
        W_out = torch.randn(B, H, 1, device=device) / math.sqrt(H)
        out = torch.bmm(h, W_out)
        
    elif prior_type < 0.66:
        # Random Forest Prior
        n_trees = torch.randint(1, 4, (1,)).item()
        depth = torch.randint(2, 5, (1,)).item()
        
        for _ in range(n_trees):
            tree_out = torch.zeros(B, N, 1, device=device)
            node_masks = [torch.ones(B, N, 1, dtype=torch.bool, device=device)]
            
            for d in range(depth):
                new_masks = []
                for mask in node_masks:
                    split_feat = torch.randint(0, K, (1,)).item()
                    feature_vals = x_input[:, :, split_feat:split_feat+1]
                    threshold = torch.randn(1, device=device) 
                    
                    left_mask = mask & (feature_vals < threshold)
                    right_mask = mask & (feature_vals >= threshold)
                    new_masks.extend([left_mask, right_mask])
                node_masks = new_masks
                
            for mask in node_masks:
                leaf_val = torch.randn(1, device=device)
                tree_out = torch.where(mask, leaf_val, tree_out)
            out += tree_out
        out /= n_trees
        
    else:
        # SCM Prior
        n_mechanisms = torch.randint(2, 6, (1,)).item()
        for _ in range(n_mechanisms):
            n_causes = torch.randint(1, min(4, K + 1), (1,)).item()
            causes_idx = torch.randperm(K)[:n_causes]
            causes = x_input[:, :, causes_idx]
            
            weights = torch.randn(B, n_causes, 1, device=device)
            linear_combo = torch.bmm(causes, weights)
            
            mech_type = torch.rand(1).item()
            if mech_type < 0.33: mech_out = torch.sin(linear_combo * torch.randn(1, device=device) * 3)
            elif mech_type < 0.66: mech_out = torch.exp(-torch.abs(linear_combo))
            else: mech_out = (linear_combo > torch.randn(1, device=device)).float()
                
            out += mech_out * torch.randn(1, device=device)

    # --- 5. LABEL DEGRADATION ---
    # Safe float32 normalization
    out = (out - out.mean(dim=1, keepdim=True)) / (out.std(dim=1, keepdim=True) + 1e-5)
    
    if torch.rand(1).item() > 0.3:
        out += torch.randn_like(out) * 0.1
        outlier_mask = (torch.rand_like(out) > 0.95).float()
        out += (torch.rand_like(out) * 6.0 - 3.0) * outlier_mask 

    # NOTE: exp() and sigmoid() transforms were removed here because they do nothing 
    # to quantiles but severely risk float truncation.
    return out

class ChemPFN(pl.LightningModule):
    def __init__(self, d_model=512, n_heads=4, n_layers=8, lr=1e-4,
                 max_classes=4, training_task="regression", d_task=32, num_bins=100):
        super().__init__()
        self.save_hyperparameters()

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

        # Freeze the base foundation model
        for param in self.chemeleon_encoder.parameters():
            param.requires_grad = False

        self.x_proj = nn.Sequential(
            nn.Linear(2_048, 2_048*2),
            nn.GELU(),
            nn.LayerNorm(2_048*2),
            nn.Linear(2_048*2, d_model - d_task)
        )

        self.y_embed_reg = nn.Embedding(num_bins, d_task)
        self.head_reg = nn.Linear(d_model, num_bins)

        self.y_embed_cls = nn.Embedding(max_classes, d_task)
        self.head_cls = nn.Linear(d_model, max_classes)

        self.query_mask_token = nn.Embedding(1, d_task)
        nn.init.normal_(self.query_mask_token.weight, mean=0.0, std=0.02)

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
        else:
            x_chemeleon = x

        x_tok = self.x_proj(x_chemeleon)

        if task == "regression":
            y_tok = self.y_embed_reg(y.clamp(min=0, max=self.hparams.num_bins - 1))
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

        x_chemeleon = x_chemeleon.view(1, -1, 2_048)

        B, N, D = 1, x_chemeleon.shape[1], x_chemeleon.shape[2]
        
        mask_prob = torch.rand(1, device=self.device).item() * 0.8 + 0.1
        query_mask = torch.rand(B, N, 1, device=self.device) > mask_prob

        n_accum = 10
        H = 32
        
        if torch.rand(1).item() < 0.25:
            K = torch.randint(1, 4, (1,)).item()
        else:
            K = torch.randint(max(5, D // 20), max(10, D // 2), (1,)).item()
            
        k_idx = torch.randperm(D, device=self.device)[:K]
        y_subset = x_chemeleon[:, :, k_idx]

        task = self.hparams.training_task

        if task == "regression":
            num_bins = self.hparams.num_bins
            loss = 0.0
            for _ in range(n_accum):
                y_hyper = _generate_synthetic_targets(y_subset, H, self.device)
                q = query_mask.squeeze(-1)
                
                # --- QUANTILE REGRESSION BINNING ---
                # y_hyper is already float32 now, but ensuring it anyway
                y_f32 = y_hyper.squeeze(-1).float()
                
                # Dynamic tie-breaking noise to prevent exact duplicates from SCM/Trees
                noise_scale = y_f32.std().item() * 1e-4 + 1e-6
                y_f32 += torch.randn_like(y_f32) * noise_scale
                
                q_probs = torch.linspace(0.0, 1.0, num_bins + 1, device=self.device, dtype=torch.float32)
                bin_edges = torch.quantile(y_f32, q_probs)
                
                # Expand outer edges slightly to catch numerical limits safely
                bin_edges[0] -= 1e-4
                bin_edges[-1] += 1e-4
                
                y_binned = torch.bucketize(y_f32, bin_edges) - 1
                y_binned = torch.clamp(y_binned, 0, num_bins - 1)

                preds = self(x_chemeleon, y_binned, query_mask, task="regression")
                
                # --- GAUSSIAN ORDINAL SMOOTHING ---
                sigma = 2.0  
                bin_indices = torch.arange(num_bins, device=self.device).float()
                
                y_true_float = y_binned[q].float().unsqueeze(-1)
                soft_labels = torch.exp(-0.5 * ((bin_indices - y_true_float) / sigma) ** 2)
                soft_labels = soft_labels / soft_labels.sum(dim=-1, keepdim=True)

                loss += F.cross_entropy(preds[q], soft_labels)
            loss /= n_accum
            
        else:
            loss = 0.0
            for _ in range(n_accum):
                y_hyper = _generate_synthetic_targets(y_subset, H, self.device)
                q = query_mask.squeeze(-1)
                
                # Must cast to float32 for torch.quantile
                context_vals = y_hyper[~q, 0].float()
                
                percentile = torch.empty(1, device=self.device).uniform_(0.1, 0.9).item()
                if context_vals.numel() > 1:
                    threshold = torch.quantile(context_vals, percentile)
                else:
                    threshold = context_vals.mean()
                    
                y_cls = (y_hyper[:, :, 0] >= threshold).long()
                
                flip_mask = torch.rand_like(y_cls.float()) < 0.03
                y_cls = torch.where(flip_mask, 1 - y_cls, y_cls)

                preds = self(x_chemeleon, y_cls, query_mask, task="classification")
                loss += F.cross_entropy(preds[..., :2][q], y_cls[q])
            loss /= n_accum
            
        self.log("train_loss", loss, prog_bar=True, on_step=True, on_epoch=True, sync_dist=True, batch_size=N)
        return loss

    def predict_step(self, batch, batch_idx, dataloader_idx=0, task="regression",
                     n_classes=None, max_context=512, n_ensemble=4):
        train_smiles, train_labels, test_smiles = batch

        if task == "regression":
            num_bins = self.hparams.num_bins
            
            # --- QUANTILE REGRESSION BINNING FOR INFERENCE ---
            labels_raw = torch.tensor(train_labels, dtype=torch.float32, device=self.device)
            
            # Add tiny tie-breaking noise to guarantee monotonic bin edges
            labels_f32 = labels_raw + torch.randn_like(labels_raw) * 1e-6 
            
            q_probs = torch.linspace(0.0, 1.0, num_bins + 1, device=self.device, dtype=torch.float32)
            bin_edges = torch.quantile(labels_f32, q_probs)
            
            bin_edges[0] -= 1e-4
            bin_edges[-1] += 1e-4
            bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2.0
            
            labels_binned = torch.bucketize(labels_raw, bin_edges) - 1
            labels_proc = torch.clamp(labels_binned, 0, num_bins - 1)
        else:
            assert n_classes is not None, "pass n_classes for classification"
            labels_proc = torch.tensor(train_labels, dtype=torch.long, device=self.device)

        all_smiles = list(train_smiles) + list(test_smiles)
        graph = featurizer(all_smiles)
        graph = _move_graph_to(graph, self.device)

        with torch.no_grad():
            self.chemeleon_encoder.eval()
            all_chemeleon = self.chemeleon_agg(self.chemeleon_encoder(graph), graph.batch).view(1, -1, 2_048)

        n_train = len(train_labels)
        n_test = len(test_smiles)
        train_x, test_x = all_chemeleon[:, :n_train], all_chemeleon[:, n_train:]
        
        min_test_budget = min(512, n_test, max(1, max_context // 4))
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

            if n_train > ctx_n:
                train_flat = train_x.squeeze(0)
                chunk_flat = X_chunk.squeeze(0)
                
                train_norm = F.normalize(train_flat, p=2, dim=-1)
                chunk_norm = F.normalize(chunk_flat, p=2, dim=-1)
                
                sim_matrix = torch.matmul(train_norm, chunk_norm.transpose(0, 1))
                relevance, _ = sim_matrix.max(dim=1)

            for _ in range(passes):
                if n_train > ctx_n:
                    top_k_n = ctx_n // 2
                    rand_n = ctx_n - top_k_n

                    if passes == 1:
                        _, top_idx = torch.topk(relevance, top_k_n)
                    else:
                        temperature = 0.05
                        u = torch.rand_like(relevance) + 1e-10
                        gumbel_noise = -torch.log(-torch.log(u))
                        noisy_relevance = (relevance / temperature) + gumbel_noise
                        _, top_idx = torch.topk(noisy_relevance, top_k_n)

                    available_mask = torch.ones(n_train, dtype=torch.bool, device=self.device)
                    available_mask[top_idx] = False
                    available_idx = torch.nonzero(available_mask).squeeze(-1)
                    
                    rand_idx = available_idx[torch.randperm(len(available_idx), device=self.device)[:rand_n]]
                    idx = torch.cat([top_idx, rand_idx])
                else:
                    idx = torch.arange(n_train, device=self.device)

                X_combined = torch.cat([train_x[:, idx], X_chunk], dim=1)
                total_len = X_combined.shape[1]
                mask = torch.zeros(1, total_len, 1, dtype=torch.bool, device=self.device)
                mask[0, len(idx):, 0] = True

                if task == "regression":
                    y_combined = torch.zeros(1, total_len, dtype=torch.long, device=self.device)
                    y_combined[0, :len(idx)] = labels_proc[idx]
                    
                    logits = self(X_combined, y_combined, mask, task="regression")[0, len(idx):, :num_bins]
                    probs = F.softmax(logits, dim=-1)
                    out = (probs * bin_centers).sum(dim=-1).view(-1, 1)
                else:
                    y_combined = torch.zeros(1, total_len, dtype=torch.long, device=self.device)
                    y_combined[0, :len(idx)] = labels_proc[idx]
                    logits = self(X_combined, y_combined, mask, task="classification")[0, len(idx):, :n_classes]
                    out = F.softmax(logits, dim=-1)

                chunk_preds += out

            preds_sum[chunk_start:chunk_end] = chunk_preds / passes

        return preds_sum

    def configure_optimizers(self):
        optimizer = torch.optim.AdamW(filter(lambda p: p.requires_grad, self.parameters()), lr=self.hparams.lr)
        total_steps = self.trainer.estimated_stepping_batches
        
        # OneCycleLR provides the critical learning rate warmup transformers need,
        # followed by the smooth cosine decay.
        scheduler = torch.optim.lr_scheduler.OneCycleLR(
            optimizer,
            max_lr=self.hparams.lr,
            total_steps=total_steps,
            pct_start=0.1,  # 10% of training spent warming up
            anneal_strategy='cos',
            div_factor=10.0,
            final_div_factor=100.0
        )
        return {
            "optimizer": optimizer,
            "lr_scheduler": {
                "scheduler": scheduler,
                "interval": "step",
            }
        }

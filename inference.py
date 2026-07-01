import torch
from model import ChemPFN

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import balanced_accuracy_score, f1_score

METRIC_FNS = {
    "balanced_accuracy": balanced_accuracy_score,
    "f1": f1_score,
}


def run_inference(
    ckpt_path,
    train_data,
    test_smiles,
    task="regression",
    n_classes=None,
    max_context=512,
    n_ensemble=4,
):
    """
    train_data:
      - regression: list of (smiles, float_label)
      - classification: list of (smiles, int_class_label)
    task: "regression" or "classification"
    n_classes: required for classification — number of classes in train_data
    """
    model = ChemPFN.load_from_checkpoint(ckpt_path)
    model.eval()

    train_smiles = [item[0] for item in train_data]
    train_labels = [item[1] for item in train_data]

    if task == "classification" and n_classes is None:
        n_classes = len(set(train_labels))

    batch = (train_smiles, train_labels, test_smiles)

    with torch.no_grad():
        predictions = model.predict_step(
            batch,
            batch_idx=0,
            task=task,
            n_classes=n_classes,
            max_context=max_context,
            n_ensemble=n_ensemble,
        )

    return predictions


def calibrate_threshold(
    ckpt_path,
    train_smiles,
    train_labels,
    metric="balanced_accuracy",
    calib_frac=0.2,
    max_context=512,
    n_ensemble=4,
    seed=42,
):
    """
    Splits train data into a context subset and a held-out calibration subset.
    Uses the context subset as in-context examples to predict on the calibration
    subset, then sweeps thresholds to find the one that maximizes `metric`
    against the known calibration labels.

    Returns: best_threshold (float)
    """
    ctx_smiles, calib_smiles, ctx_labels, calib_labels = train_test_split(
        train_smiles,
        train_labels,
        test_size=calib_frac,
        random_state=seed,
        stratify=train_labels,  # keep class balance in both splits
    )

    calib_probs = run_inference(
        ckpt_path,
        list(zip(ctx_smiles, ctx_labels)),
        calib_smiles,
        task="classification",
        n_classes=2,
        max_context=max_context,
        n_ensemble=n_ensemble,
    )[:, 1].numpy(force=True)

    calib_labels = np.array(calib_labels)
    metric_fn = METRIC_FNS[metric]

    best_threshold, best_score = 0.5, -np.inf
    for t in np.arange(0.05, 0.96, 0.01):
        preds = (calib_probs >= t).astype(int)
        # skip degenerate thresholds where one class disappears entirely
        if len(np.unique(preds)) < 2:
            continue
        score = metric_fn(calib_labels, preds)
        if score > best_score:
            best_score, best_threshold = score, t

    return best_threshold, best_score


if __name__ == "__main__":
    import sys

    try:
        ckpt_path = sys.argv[1]
    except IndexError:
        print("usage: python inference.py /path/to/model.ckpt")
        exit(1)

    # --- Regression example ---
    train_set_reg = [("CCO", -1.0), ("CCN", -0.5), ("CCC", -2.1), ("CCCC", -2.9)]
    test_set_reg = ["CCCCC", "CCO"]
    reg_preds = run_inference(ckpt_path, train_set_reg, test_set_reg, task="regression")
    print("In-Context Predicted Solubility:", reg_preds.squeeze().tolist())

    # --- Classification example ---
    train_set_cls = [("CCO", 0), ("CCN", 1), ("CCC", 0), ("c1ccccc1N", 1)]
    test_set_cls = ["CCCC", "c1ccccc1"]
    cls_probs = run_inference(
        ckpt_path, train_set_cls, test_set_cls, task="classification", n_classes=2
    )
    print("Class probabilities:\n", cls_probs)
    print("Predicted classes:", cls_probs.argmax(dim=-1).tolist())
    print("Predicted binary probability:", cls_probs.softmax(dim=0)[:, 1].tolist())

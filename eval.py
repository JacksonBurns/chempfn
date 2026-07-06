import datetime
import json
import sys

import polaris as po
from polaris.utils.types import TargetType

from inference import run_inference, calibrate_threshold

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: python eval.py /path/to/reg_model.ckpt /path/to/cls_model.ckpt")
        exit(1)

    reg_ckpt, cls_ckpt = sys.argv[1], sys.argv[2]

    output_file = open("eval_results.md", "w")
    output_file.write(
        f"""# Eval Results

timestamp: {datetime.datetime.now()}
reg_checkpoint: {reg_ckpt}
cls_checkpoint: {cls_ckpt}
"""
    )
    performance_dict = {}
    polaris_benchmarks = (
        "polaris/pkis2-ret-wt-cls-v2",
        "polaris/pkis2-ret-wt-reg-v2",
        "polaris/pkis2-kit-wt-cls-v2",
        "polaris/pkis2-kit-wt-reg-v2",
        "polaris/pkis2-egfr-wt-reg-v2",
        "polaris/adme-fang-solu-1",
        "polaris/adme-fang-rppb-1",
        "polaris/adme-fang-hppb-1",
        "polaris/adme-fang-perm-1",
        "polaris/adme-fang-rclint-1",
        "polaris/adme-fang-hclint-1",
        "tdcommons/lipophilicity-astrazeneca",
        "tdcommons/ppbr-az",
        "tdcommons/clearance-hepatocyte-az",
        "tdcommons/cyp2d6-substrate-carbonmangels",
        "tdcommons/half-life-obach",
        "tdcommons/cyp2c9-substrate-carbonmangels",
        "tdcommons/clearance-microsome-az",
        "tdcommons/dili",
        "tdcommons/bioavailability-ma",
        "tdcommons/vdss-lombardo",
        "tdcommons/cyp3a4-substrate-carbonmangels",
        "tdcommons/pgp-broccatelli",
        "tdcommons/caco2-wang",
        "tdcommons/herg",
        "tdcommons/bbb-martins",
        "tdcommons/ames",
        "tdcommons/ld50-zhu",
    )
    for benchmark_name in polaris_benchmarks:
        benchmark = po.load_benchmark(benchmark_name)
        smiles_col = list(benchmark.input_cols)[0]
        target_cols = list(benchmark.target_cols)
        train, test = benchmark.get_train_test_split()
        train_df, test_df = train.as_dataframe(), test.as_dataframe()
        task_type = benchmark.target_types[target_cols[0]]

        train_smiles_list = train_df[smiles_col].to_list()
        train_labels_list = train_df[target_cols[0]].to_list()

        # Select checkpoint based on task type
        ckpt_path = reg_ckpt if task_type == TargetType.REGRESSION else cls_ckpt

        threshold = 0.5
        if task_type == TargetType.CLASSIFICATION:
            threshold, calib_score = calibrate_threshold(
                ckpt_path,
                train_smiles_list,
                train_labels_list,
                metric="balanced_accuracy",
            )
            print(f"[{benchmark_name}] calibrated threshold={threshold:.2f} "
                  f"(calib balanced_accuracy={calib_score:.3f})")

        predictions = run_inference(
            ckpt_path,
            list(zip(train_smiles_list, train_labels_list)),
            test_df[smiles_col].to_list(),
            task="regression" if task_type == TargetType.REGRESSION else "classification",
            n_classes=None if task_type == TargetType.REGRESSION else 2,
        )

        if task_type == TargetType.CLASSIFICATION:
            probs_pos = predictions[:, 1].numpy(force=True)
            y_pred = (probs_pos >= threshold).astype(int)
            results = benchmark.evaluate(y_pred, probs_pos).results
            performance = results.query(
                f"Metric == '{benchmark.main_metric.label}'"
            )["Score"].values[0]
        elif task_type == TargetType.REGRESSION:
            results = benchmark.evaluate(predictions.numpy(force=True).flatten()).results
            performance = results.query(
                f"Metric == '{benchmark.main_metric.label}'"
            )["Score"].values[0]

        output_file.write(
            f"""
## `{benchmark_name}`{f"\n\ncalibrated threshold: {threshold:.2f}\n" if task_type == TargetType.CLASSIFICATION else "\n"}
{results.to_markdown()}
"""
        )
        performance_dict[benchmark_name] = {benchmark.main_metric.label: performance}

    output_file.write(
        f"""
# Summary

results_dict = {json.dumps(performance_dict, indent=4)}
"""
    )

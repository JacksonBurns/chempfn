# Eval Results
timestamp: 2026-07-01 08:15:58.094502


## `polaris/pkis2-ret-wt-cls-v2`

calibrated threshold: 0.89

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.516129 |
|  1 | test       | CLS_RET        | accuracy    | 0.858491 |
|  2 | test       | CLS_RET        | mcc         | 0.436971 |
|  3 | test       | CLS_RET        | pr_auc      | 0.501354 |
|  4 | test       | CLS_RET        | roc_auc     | 0.797092 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.434164 |

## `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.534939 |
|  1 | test       | RET            | explained_var       |   0.297584 |
|  2 | test       | RET            | mean_absolute_error |  22.151    |
|  3 | test       | RET            | mean_squared_error  | 953.956    |
|  4 | test       | RET            | r2                  |   0.196605 |
|  5 | test       | RET            | pearsonr            |   0.563219 |

## `polaris/pkis2-kit-wt-cls-v2`

calibrated threshold: 0.82

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.45614  |
|  1 | test       | CLS_KIT        | accuracy    | 0.732759 |
|  2 | test       | CLS_KIT        | mcc         | 0.304793 |
|  3 | test       | CLS_KIT        | pr_auc      | 0.527771 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.779497 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.291009 |

## `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.493824 |
|  1 | test       | KIT            | explained_var       |   0.25842  |
|  2 | test       | KIT            | mean_absolute_error |  24.4107   |
|  3 | test       | KIT            | mean_squared_error  | 902.881    |
|  4 | test       | KIT            | r2                  |   0.251767 |
|  5 | test       | KIT            | pearsonr            |   0.51358  |

## `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.253043 |
|  1 | test       | EGFR           | explained_var       |   0.332429 |
|  2 | test       | EGFR           | mean_absolute_error |  18.3563   |
|  3 | test       | EGFR           | mean_squared_error  | 538.585    |
|  4 | test       | EGFR           | r2                  |   0.331588 |
|  5 | test       | EGFR           | pearsonr            |   0.582934 |

## `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.441754 |
|  1 | test       | LOG_SOLUBILITY | explained_var       | 0.254168 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.425602 |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.430961 |
|  4 | test       | LOG_SOLUBILITY | r2                  | 0.205132 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.51098  |

## `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.755652 |
|  1 | test       | LOG_RPPB       | explained_var       | 0.626548 |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.432688 |
|  3 | test       | LOG_RPPB       | mean_squared_error  | 0.33481  |
|  4 | test       | LOG_RPPB       | r2                  | 0.623166 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.802026 |

## `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.822676 |
|  1 | test       | LOG_HPPB       | explained_var       | 0.697186 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.324393 |
|  3 | test       | LOG_HPPB       | mean_squared_error  | 0.191817 |
|  4 | test       | LOG_HPPB       | r2                  | 0.683281 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.835468 |

## `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.698409 |
|  1 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.459722 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.395527 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.270023 |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.454931 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.686769 |

## `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.603039 |
|  1 | test       | LOG_RLM_CLint  | explained_var       | 0.362719 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.487423 |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.36092  |
|  4 | test       | LOG_RLM_CLint  | r2                  | 0.360686 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.605914 |

## `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.577465 |
|  1 | test       | LOG_HLM_CLint  | explained_var       | 0.320456 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.412906 |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.276476 |
|  4 | test       | LOG_HLM_CLint  | r2                  | 0.288184 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.566421 |

## `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.666864 |

## `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.12443 |

## `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.409241 |

## `tdcommons/cyp2d6-substrate-carbonmangels`

calibrated threshold: 0.79

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.680872 |

## `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.349625 |

## `tdcommons/cyp2c9-substrate-carbonmangels`

calibrated threshold: 0.72

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.402335 |

## `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.601529 |

## `tdcommons/dili`

calibrated threshold: 0.33

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.878696 |

## `tdcommons/bioavailability-ma`

calibrated threshold: 0.11

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.642501 |

## `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.379135 |

## `tdcommons/cyp3a4-substrate-carbonmangels`

calibrated threshold: 0.48

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.674051 |

## `tdcommons/pgp-broccatelli`

calibrated threshold: 0.42

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.921821 |

## `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.332646 |

## `tdcommons/herg`

calibrated threshold: 0.20

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.827982 |

## `tdcommons/bbb-martins`

calibrated threshold: 0.07

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.879143 |

## `tdcommons/ames`

calibrated threshold: 0.41

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.793111 |

## `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.701051 |

# Summary

results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": {
        "pr_auc": 0.5013543534351208
    },
    "polaris/pkis2-ret-wt-reg-v2": {
        "mean_squared_error": 953.9557057693766
    },
    "polaris/pkis2-kit-wt-cls-v2": {
        "pr_auc": 0.5277714899503864
    },
    "polaris/pkis2-kit-wt-reg-v2": {
        "mean_squared_error": 902.8812884237173
    },
    "polaris/pkis2-egfr-wt-reg-v2": {
        "mean_squared_error": 538.5851208229027
    },
    "polaris/adme-fang-solu-1": {
        "pearsonr": 0.5109795094506964
    },
    "polaris/adme-fang-rppb-1": {
        "pearsonr": 0.8020261011452127
    },
    "polaris/adme-fang-hppb-1": {
        "pearsonr": 0.8354684878954554
    },
    "polaris/adme-fang-perm-1": {
        "pearsonr": 0.6867687184774326
    },
    "polaris/adme-fang-rclint-1": {
        "pearsonr": 0.6059138855584476
    },
    "polaris/adme-fang-hclint-1": {
        "pearsonr": 0.5664206805942509
    },
    "tdcommons/lipophilicity-astrazeneca": {
        "mean_absolute_error": 0.6668643958057676
    },
    "tdcommons/ppbr-az": {
        "mean_absolute_error": 8.124428443158036
    },
    "tdcommons/clearance-hepatocyte-az": {
        "spearmanr": 0.40924145256683564
    },
    "tdcommons/cyp2d6-substrate-carbonmangels": {
        "pr_auc": 0.6808718822041566
    },
    "tdcommons/half-life-obach": {
        "spearmanr": 0.3496246308536596
    },
    "tdcommons/cyp2c9-substrate-carbonmangels": {
        "pr_auc": 0.402334912695236
    },
    "tdcommons/clearance-microsome-az": {
        "spearmanr": 0.6015288585074815
    },
    "tdcommons/dili": {
        "roc_auc": 0.8786956521739131
    },
    "tdcommons/bioavailability-ma": {
        "roc_auc": 0.6425008313934154
    },
    "tdcommons/vdss-lombardo": {
        "spearmanr": 0.37913518619026926
    },
    "tdcommons/cyp3a4-substrate-carbonmangels": {
        "roc_auc": 0.6740506329113924
    },
    "tdcommons/pgp-broccatelli": {
        "roc_auc": 0.9218208477739269
    },
    "tdcommons/caco2-wang": {
        "mean_absolute_error": 0.3326460891342331
    },
    "tdcommons/herg": {
        "roc_auc": 0.8279823269513992
    },
    "tdcommons/bbb-martins": {
        "roc_auc": 0.8791432145090682
    },
    "tdcommons/ames": {
        "roc_auc": 0.7931112808161507
    },
    "tdcommons/ld50-zhu": {
        "mean_absolute_error": 0.7010512210938862
    }
}

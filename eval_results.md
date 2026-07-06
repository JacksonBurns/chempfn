# Eval Results
timestamp: 2026-07-06 09:56:53.982746


## `polaris/pkis2-ret-wt-cls-v2`

calibrated threshold: 0.44

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.529412 |
|  1 | test       | CLS_RET        | pr_auc      | 0.542853 |
|  2 | test       | CLS_RET        | mcc         | 0.439524 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.439524 |
|  4 | test       | CLS_RET        | roc_auc     | 0.808328 |
|  5 | test       | CLS_RET        | accuracy    | 0.849057 |

## `polaris/pkis2-ret-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.559285 |
|  1 | test       | RET            | r2                  |   0.264238 |
|  2 | test       | RET            | explained_var       |   0.41459  |
|  3 | test       | RET            | pearsonr            |   0.653011 |
|  4 | test       | RET            | mean_squared_error  | 873.647    |
|  5 | test       | RET            | mean_absolute_error |  21.404    |

## `polaris/pkis2-kit-wt-cls-v2`

calibrated threshold: 0.46

|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.415094 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.484154 |
|  2 | test       | CLS_KIT        | mcc         | 0.254461 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.248328 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.767892 |
|  5 | test       | CLS_KIT        | accuracy    | 0.732759 |

## `polaris/pkis2-kit-wt-reg-v2`

|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | KIT            | spearmanr           |    0.362531  |
|  1 | test       | KIT            | r2                  |    0.0757013 |
|  2 | test       | KIT            | explained_var       |    0.101781  |
|  3 | test       | KIT            | pearsonr            |    0.392172  |
|  4 | test       | KIT            | mean_squared_error  | 1115.34      |
|  5 | test       | KIT            | mean_absolute_error |   26.5665    |

## `polaris/pkis2-egfr-wt-reg-v2`

|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.29081  |
|  1 | test       | EGFR           | r2                  |   0.295448 |
|  2 | test       | EGFR           | explained_var       |   0.315035 |
|  3 | test       | EGFR           | pearsonr            |   0.561508 |
|  4 | test       | EGFR           | mean_squared_error  | 567.706    |
|  5 | test       | EGFR           | mean_absolute_error |  18.8603   |

## `polaris/adme-fang-solu-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.476719 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.279149 |
|  2 | test       | LOG_SOLUBILITY | explained_var       | 0.282077 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.531347 |
|  4 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.39083  |
|  5 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.442525 |

## `polaris/adme-fang-rppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.74     |
|  1 | test       | LOG_RPPB       | r2                  | 0.686746 |
|  2 | test       | LOG_RPPB       | explained_var       | 0.692333 |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.836231 |
|  4 | test       | LOG_RPPB       | mean_squared_error  | 0.278321 |
|  5 | test       | LOG_RPPB       | mean_absolute_error | 0.382842 |

## `polaris/adme-fang-hppb-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.776072 |
|  1 | test       | LOG_HPPB       | r2                  | 0.462738 |
|  2 | test       | LOG_HPPB       | explained_var       | 0.547055 |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.766151 |
|  4 | test       | LOG_HPPB       | mean_squared_error  | 0.325387 |
|  5 | test       | LOG_HPPB       | mean_absolute_error | 0.421981 |

## `polaris/adme-fang-perm-1`

|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.739798 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.499186 |
|  2 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.508318 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.715557 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.2481   |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.370196 |

## `polaris/adme-fang-rclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.606944 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.369612 |
|  2 | test       | LOG_RLM_CLint  | explained_var       | 0.369663 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.608216 |
|  4 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.355881 |
|  5 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.475614 |

## `polaris/adme-fang-hclint-1`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.581449 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.310952 |
|  2 | test       | LOG_HLM_CLint  | explained_var       | 0.325222 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.572839 |
|  4 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.267633 |
|  5 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.409681 |

## `tdcommons/lipophilicity-astrazeneca`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.693141 |

## `tdcommons/ppbr-az`

|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.43124 |

## `tdcommons/clearance-hepatocyte-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.419178 |

## `tdcommons/cyp2d6-substrate-carbonmangels`

calibrated threshold: 0.56

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.723286 |

## `tdcommons/half-life-obach`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.140856 |

## `tdcommons/cyp2c9-substrate-carbonmangels`

calibrated threshold: 0.35

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.397067 |

## `tdcommons/clearance-microsome-az`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.525481 |

## `tdcommons/dili`

calibrated threshold: 0.51

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.873913 |

## `tdcommons/bioavailability-ma`

calibrated threshold: 0.75

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.728633 |

## `tdcommons/vdss-lombardo`

|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.384162 |

## `tdcommons/cyp3a4-substrate-carbonmangels`

calibrated threshold: 0.74

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.690099 |

## `tdcommons/pgp-broccatelli`

calibrated threshold: 0.53

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.924154 |

## `tdcommons/caco2-wang`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.348575 |

## `tdcommons/herg`

calibrated threshold: 0.70

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.847128 |

## `tdcommons/bbb-martins`

calibrated threshold: 0.63

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.910569 |

## `tdcommons/ames`

calibrated threshold: 0.56

|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.795906 |

## `tdcommons/ld50-zhu`

|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.728376 |

# Summary

results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": {
        "pr_auc": 0.5428525451757954
    },
    "polaris/pkis2-ret-wt-reg-v2": {
        "mean_squared_error": 873.6469523220944
    },
    "polaris/pkis2-kit-wt-cls-v2": {
        "pr_auc": 0.48415403477993124
    },
    "polaris/pkis2-kit-wt-reg-v2": {
        "mean_squared_error": 1115.3364589011296
    },
    "polaris/pkis2-egfr-wt-reg-v2": {
        "mean_squared_error": 567.7057355581196
    },
    "polaris/adme-fang-solu-1": {
        "pearsonr": 0.5313470409023221
    },
    "polaris/adme-fang-rppb-1": {
        "pearsonr": 0.8362312411386982
    },
    "polaris/adme-fang-hppb-1": {
        "pearsonr": 0.7661507777506577
    },
    "polaris/adme-fang-perm-1": {
        "pearsonr": 0.715556880016324
    },
    "polaris/adme-fang-rclint-1": {
        "pearsonr": 0.6082156375815962
    },
    "polaris/adme-fang-hclint-1": {
        "pearsonr": 0.5728389766282893
    },
    "tdcommons/lipophilicity-astrazeneca": {
        "mean_absolute_error": 0.6931411628439312
    },
    "tdcommons/ppbr-az": {
        "mean_absolute_error": 8.431237082711698
    },
    "tdcommons/clearance-hepatocyte-az": {
        "spearmanr": 0.41917766637072257
    },
    "tdcommons/cyp2d6-substrate-carbonmangels": {
        "pr_auc": 0.7232861045580454
    },
    "tdcommons/half-life-obach": {
        "spearmanr": 0.14085572072635646
    },
    "tdcommons/cyp2c9-substrate-carbonmangels": {
        "pr_auc": 0.3970672945899606
    },
    "tdcommons/clearance-microsome-az": {
        "spearmanr": 0.5254806881665962
    },
    "tdcommons/dili": {
        "roc_auc": 0.8739130434782609
    },
    "tdcommons/bioavailability-ma": {
        "roc_auc": 0.7286331892251413
    },
    "tdcommons/vdss-lombardo": {
        "spearmanr": 0.38416206336670705
    },
    "tdcommons/cyp3a4-substrate-carbonmangels": {
        "roc_auc": 0.6900994575045208
    },
    "tdcommons/pgp-broccatelli": {
        "roc_auc": 0.9241535590509198
    },
    "tdcommons/caco2-wang": {
        "mean_absolute_error": 0.3485745927456029
    },
    "tdcommons/herg": {
        "roc_auc": 0.8471281296023564
    },
    "tdcommons/bbb-martins": {
        "roc_auc": 0.910569105691057
    },
    "tdcommons/ames": {
        "roc_auc": 0.795905539564119
    },
    "tdcommons/ld50-zhu": {
        "mean_absolute_error": 0.7283755630111178
    }
}

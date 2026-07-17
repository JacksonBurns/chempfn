# Eval Results

timestamp: 2026-07-17 09:44:35.730421
reg_checkpoint: reg.ckpt
cls_checkpoint: cls.ckpt

## `polaris/pkis2-ret-wt-cls-v2`

### Model Performance
|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.886792 |
|  1 | test       | CLS_RET        | roc_auc     | 0.853933 |
|  2 | test       | CLS_RET        | mcc         | 0.560157 |
|  3 | test       | CLS_RET        | cohen_kappa | 0.55864  |
|  4 | test       | CLS_RET        | pr_auc      | 0.646648 |
|  5 | test       | CLS_RET        | f1          | 0.625    |

### Leaderboard Comparison
| Name                                 |   pr_auc |
|:-------------------------------------|---------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics   | 0.885    |
| 1B_MolGPS-ens_LargeMix-and-Phenomics | 0.879    |
| ChemPFN                              | 0.646648 |
| CheMeleon                            | 0.639    |
| MHNfs                                | 0.417    |

## `polaris/pkis2-ret-wt-reg-v2`

### Model Performance
|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | pearsonr            |   0.58216  |
|  1 | test       | RET            | spearmanr           |   0.535299 |
|  2 | test       | RET            | r2                  |   0.239089 |
|  3 | test       | RET            | explained_var       |   0.280045 |
|  4 | test       | RET            | mean_absolute_error |  23.2754   |
|  5 | test       | RET            | mean_squared_error  | 903.509    |

### Leaderboard Comparison
| Name                                 |   mean_squared_error |
|:-------------------------------------|---------------------:|
| 1B_MolGPS-ens_LargeMix-and-Phenomics |              589.944 |
| 3B_e50_MPNN_LargeMix-and-Phenomics   |              609.399 |
| CheMeleon                            |              684.319 |
| CheMeleon                            |              724.347 |
| ChemPFN                              |              903.509 |

## `polaris/pkis2-kit-wt-cls-v2`

### Model Performance
|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.827586 |
|  1 | test       | CLS_KIT        | roc_auc     | 0.795455 |
|  2 | test       | CLS_KIT        | mcc         | 0.517781 |
|  3 | test       | CLS_KIT        | cohen_kappa | 0.50764  |
|  4 | test       | CLS_KIT        | pr_auc      | 0.614834 |
|  5 | test       | CLS_KIT        | f1          | 0.615385 |

### Leaderboard Comparison
| Name      |   pr_auc |
|:----------|---------:|
| CheMeleon | 0.646    |
| ChemPFN   | 0.614834 |
| MHNfs     | 0.376    |

## `polaris/pkis2-kit-wt-reg-v2`

### Model Performance
|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | pearsonr            |   0.537992 |
|  1 | test       | KIT            | spearmanr           |   0.440063 |
|  2 | test       | KIT            | r2                  |   0.242053 |
|  3 | test       | KIT            | explained_var       |   0.287658 |
|  4 | test       | KIT            | mean_absolute_error |  23.0616   |
|  5 | test       | KIT            | mean_squared_error  | 914.602    |

### Leaderboard Comparison
| Name      |   mean_squared_error |
|:----------|---------------------:|
| CheMeleon |              849.611 |
| ChemPFN   |              914.602 |

## `polaris/pkis2-egfr-wt-reg-v2`

### Model Performance
|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | pearsonr            |   0.654715 |
|  1 | test       | EGFR           | spearmanr           |   0.34211  |
|  2 | test       | EGFR           | r2                  |   0.380339 |
|  3 | test       | EGFR           | explained_var       |   0.38601  |
|  4 | test       | EGFR           | mean_absolute_error |  17.4944   |
|  5 | test       | EGFR           | mean_squared_error  | 499.303    |

### Leaderboard Comparison
| Name                                   |   mean_squared_error |
|:---------------------------------------|---------------------:|
| aether-pharmaos-pkis2-egfr-wt-ensemble |              430.821 |
| CheMeleon                              |              459.929 |
| ChemPFN                                |              499.303 |

## `polaris/adme-fang-solu-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | pearsonr            | 0.619319 |
|  1 | test       | LOG_SOLUBILITY | spearmanr           | 0.492713 |
|  2 | test       | LOG_SOLUBILITY | r2                  | 0.365266 |
|  3 | test       | LOG_SOLUBILITY | explained_var       | 0.365307 |
|  4 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.419353 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.344139 |

### Leaderboard Comparison
| Name                        |   pearsonr |
|:----------------------------|-----------:|
| 1B_MPNN_MolGPS-ens_LargeMix |   0.77     |
| 1B_MPNN_LargeMix-Phenomics  |   0.764    |
| CheMeleonMOE                |   0.729    |
| CheMeleon                   |   0.682    |
| it-works-now                |   0.669    |
| ML4DD-team16                |   0.654    |
| ML4DD-team9                 |   0.651    |
| team9_submission_2          |   0.651    |
| ExactTanimotoGP             |   0.635    |
| ML4DD-team25                |   0.632    |
| ChemPFN                     |   0.619319 |

## `polaris/adme-fang-rppb-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | pearsonr            | 0.853979 |
|  1 | test       | LOG_RPPB       | spearmanr           | 0.9      |
|  2 | test       | LOG_RPPB       | r2                  | 0.684386 |
|  3 | test       | LOG_RPPB       | explained_var       | 0.689104 |
|  4 | test       | LOG_RPPB       | mean_absolute_error | 0.390664 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.280418 |

### Leaderboard Comparison
| Name                                          |   pearsonr |
|:----------------------------------------------|-----------:|
| 1B_MPNN_LargeMix-and-Phenomics                |   0.908    |
| 1B_MPNN_MolGPS-ens_LargeMix                   |   0.886    |
| nepare                                        |   0.863    |
| ChemPFN                                       |   0.853979 |
| TabPFNv2-rdkit                                |   0.816    |
| nepare_chemprop                               |   0.78     |
| chemma-2b-sft                                 |   0.747    |
| adme-fang-RPPB-1_desc2D_RandomForestRegressor |   0.722    |
| adme-fang-RPPB-1-GIRAFFE-wae                  |   0.68     |
| CheMeleon                                     |   0.662    |
| chemlactica-1b-sft                            |   0.614    |

## `polaris/adme-fang-hppb-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | pearsonr            | 0.828275 |
|  1 | test       | LOG_HPPB       | spearmanr           | 0.829093 |
|  2 | test       | LOG_HPPB       | r2                  | 0.636636 |
|  3 | test       | LOG_HPPB       | explained_var       | 0.682283 |
|  4 | test       | LOG_HPPB       | mean_absolute_error | 0.374763 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.220067 |

### Leaderboard Comparison
| Name                                            |   pearsonr |
|:------------------------------------------------|-----------:|
| 1B_MPNN_LargeMix-and-Phenomics                  |   0.888    |
| 1B_MPNN_MolGPS-ens_LargeMix                     |   0.884    |
| ChemPFN                                         |   0.828275 |
| TabPFNv2-rdkit                                  |   0.827    |
| adme-fang-HPPB-1-GIRAFFE-wae                    |   0.815    |
| agentomics-ml-adme-fang-hppb-1                  |   0.815    |
| nepare                                          |   0.809    |
| CheMeleon                                       |   0.793    |
| chemlactica-125m-sft                            |   0.774    |
| adme-fang-HPPB-1_atompair_RandomForestRegressor |   0.69     |
| chemma-2b-sft                                   |   0.636    |

## `polaris/adme-fang-perm-1`

### Model Performance
|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.741203 |
|  1 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.741801 |
|  2 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.526831 |
|  3 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.529892 |
|  4 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.379551 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.234405 |

### Leaderboard Comparison
| Name                                          |   pearsonr |
|:----------------------------------------------|-----------:|
| 1B_MPNN_MolGPS-ens_LargeMix                   |   0.879    |
| 1B_MPNN_LargeMix-and-Phenomics                |   0.86     |
| CheMeleon                                     |   0.822    |
| MolEncoder                                    |   0.804    |
| TabPFNv2-rdkit                                |   0.798    |
| adme-fang-PERM-1-GIRAFFE-wae_s                |   0.772    |
| chemlactica-1b-sft                            |   0.762    |
| ChemPFN                                       |   0.741203 |
| optimized-random-forest-rdkit-descriptors     |   0.727    |
| adme-fang-PERM-1_desc2D_RandomForestRegressor |   0.716    |
| chemlactica-125m-sft                          |   0.714    |

## `polaris/adme-fang-rclint-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | pearsonr            | 0.633309 |
|  1 | test       | LOG_RLM_CLint  | spearmanr           | 0.629493 |
|  2 | test       | LOG_RLM_CLint  | r2                  | 0.391893 |
|  3 | test       | LOG_RLM_CLint  | explained_var       | 0.391894 |
|  4 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.480343 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.343303 |

### Leaderboard Comparison
| Name                                            |   pearsonr |
|:------------------------------------------------|-----------:|
| 1B_MPNN_MolGPS-ens_LargeMix                     |   0.798    |
| 1B_MPNN_LargeMix-and-Phenomics                  |   0.784    |
| CheMeleon                                       |   0.757    |
| chemlactica-125m-sft                            |   0.714    |
| chemlactica-1b-sft                              |   0.698    |
| TabPFNv2-rdkit                                  |   0.694    |
| chemma-2b-sft                                   |   0.66     |
| adme-fang-RCLint-1_desc2D_RandomForestRegressor |   0.64     |
| ChemPFN                                         |   0.633309 |
| adme-fang-RCLint-1_desc2D_RandomForestRegressor |   0.631    |
| adme-fang-RCLint-1_desc2D_FCModel               |   0.544    |

## `polaris/adme-fang-hclint-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | pearsonr            | 0.630078 |
|  1 | test       | LOG_HLM_CLint  | spearmanr           | 0.621483 |
|  2 | test       | LOG_HLM_CLint  | r2                  | 0.379064 |
|  3 | test       | LOG_HLM_CLint  | explained_var       | 0.379944 |
|  4 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.402292 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.241178 |

### Leaderboard Comparison
| Name                                            |   pearsonr |
|:------------------------------------------------|-----------:|
| seqera-gradient                                 |   0.796    |
| 1B_MPNN_LargeMix-and-Phenomics                  |   0.778    |
| chemlactica-1b-sft                              |   0.72     |
| CheMeleon                                       |   0.72     |
| chemlactica-125m-sft                            |   0.717    |
| MolEncoder                                      |   0.714    |
| agentomics-ml-adme-fang-hclint-1                |   0.697    |
| chemma-2b-sft                                   |   0.674    |
| TabPFNv2-rdkit                                  |   0.662    |
| adme-fang-HCLint-1_desc2D_RandomForestRegressor |   0.639    |
| ChemPFN                                         |   0.630078 |

## `tdcommons/lipophilicity-astrazeneca`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.717933 |

### Leaderboard Comparison
| Name                                      |   mean_absolute_error |
|:------------------------------------------|----------------------:|
| 1B_MPNN_MolGPS-ens_LargeMix-and-Phenomics |              0.392    |
| 1B_MPNN_LargeMix-and-Phenomics            |              0.411    |
| 3B_e50_MPNN_LargeMix-and-Phenomics        |              0.424    |
| CheMeleon                                 |              0.443    |
| MolEncoder                                |              0.497    |
| agentomics-ml-lipophilicity-astrazeneca   |              0.497    |
| TabPFNv2-rdkit                            |              0.499    |
| TabPFNv2-rdkit                            |              0.502    |
| TabPFNv2-maplight_gnn                     |              0.502    |
| TabPFNv2-rdkit-3D                         |              0.524    |
| ChemPFN                                   |              0.717933 |

## `tdcommons/ppbr-az`

### Model Performance
|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.67746 |

### Leaderboard Comparison
| Name                               |   mean_absolute_error |
|:-----------------------------------|----------------------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics |               7.004   |
| 1B_MPNN_LargeMix-and-Phenomics     |               7.026   |
| TabPFNv2-rdkit-3D                  |               7.033   |
| TabPFNv2-rdkit                     |               7.117   |
| CheMeleon                          |               7.532   |
| ChemPFN                            |               8.67746 |

## `tdcommons/clearance-hepatocyte-az`

### Model Performance
|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.369156 |

### Leaderboard Comparison
| Name                                |   spearmanr |
|:------------------------------------|------------:|
| 1B_MPNN_LargeMix-and-Phenomics      |    0.538    |
| 3B_e50_MPNN_LargeMix-and-Phenomics  |    0.525    |
| clearance-hepatocyte-az-GIRAFFE-wae |    0.429    |
| TabPFNv2-rdkit                      |    0.41     |
| TabPFNv2-rdkit-3D                   |    0.402    |
| CheMeleon                           |    0.387    |
| ChemPFN                             |    0.369156 |

## `tdcommons/cyp2d6-substrate-carbonmangels`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.607075 |

### Leaderboard Comparison
| Name                                         |   pr_auc |
|:---------------------------------------------|---------:|
| aether-pharmaos-cyp2d6-sub-3d-ensemble       | 0.732    |
| drylab                                       | 0.724    |
| No name provided                             | 0.719    |
| TabPFNv2-rdkit                               | 0.717    |
| TabPFNv2-rdkit-3D                            | 0.714    |
| 1B_MPNN_LargeMix-and-Phenomics               | 0.711    |
| agentomics-ml-cyp2d6-substrate-carbonmangels | 0.707    |
| CheMeleon                                    | 0.688    |
| 3B_e50_MPNN_LargeMix-and-Phenomics           | 0.68     |
| ChemPFN                                      | 0.607075 |
| ARKA-Mordred                                 | 0.558    |

## `tdcommons/half-life-obach`

### Model Performance
|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.496956 |

### Leaderboard Comparison
| Name                               |   spearmanr |
|:-----------------------------------|------------:|
| 1B_MPNN_LargeMix-and-Phenomics     |    0.625    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |    0.573    |
| TabPFNv2-rdkit                     |    0.542    |
| ChemPFN                            |    0.496956 |
| TabPFNv2-rdkit-3D                  |    0.489    |
| MolEncoder                         |    0.417    |
| CheMeleon                          |    0.36     |

## `tdcommons/cyp2c9-substrate-carbonmangels`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.395266 |

### Leaderboard Comparison
| Name                               |   pr_auc |
|:-----------------------------------|---------:|
| 1B_MPNN_LargeMix-and-Phenomics     | 0.478    |
| CheMeleon                          | 0.47     |
| 3B_e50_MPNN_LargeMix-and-Phenomics | 0.407    |
| ChemPFN                            | 0.395266 |
| TabPFNv2-rdkit                     | 0.378    |
| MHNfs                              | 0.276    |

## `tdcommons/clearance-microsome-az`

### Model Performance
|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.571483 |

### Leaderboard Comparison
| Name                               |   spearmanr |
|:-----------------------------------|------------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics |    0.683    |
| 1B_MPNN_LargeMix-and-Phenomics     |    0.653    |
| TabPFNv2-rdkit-3D                  |    0.649    |
| TabPFNv2-rdkit                     |    0.64     |
| CheMeleon                          |    0.59     |
| ChemPFN                            |    0.571483 |

## `tdcommons/dili`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.936957 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| ChemPFN                            |  0.936957 |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.933    |
| vidraft-structure-ensemble-dili    |  0.933    |
| TabPFNv2-rdkit-3D                  |  0.93     |
| 1B_MPNN_LargeMix-and-Phenomics     |  0.925    |
| CheMeleon                          |  0.916    |
| TabPFNv2-rdkit                     |  0.9      |

## `tdcommons/bioavailability-ma`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.671101 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| vidraft-tabpfn-ensemble-bioavail   |  0.734    |
| TabPFNv2-rdkit-3D                  |  0.729    |
| TabPFNv2-rdkit                     |  0.728    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.714    |
| CheMeleon                          |  0.698    |
| 1B_MPNN_LargeMix-and-Phenomics     |  0.675    |
| ChemPFN                            |  0.671101 |
| MHNfs                              |  0.61     |

## `tdcommons/vdss-lombardo`

### Model Performance
|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.572601 |

### Leaderboard Comparison
| Name                               |   spearmanr |
|:-----------------------------------|------------:|
| vidraft-tabpfn-vdss                |    0.726    |
| TabPFNv2-rdkit                     |    0.7      |
| TabPFNv2-rdkit-3D                  |    0.69     |
| 1B_MPNN_LargeMix-and-Phenomics     |    0.637    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |    0.6      |
| CheMeleon                          |    0.59     |
| ChemPFN                            |    0.572601 |

## `tdcommons/cyp3a4-substrate-carbonmangels`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.637432 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| 1B_MPNN_LargeMix-and-Phenomics     |  0.696    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.685    |
| ChemPFN                            |  0.637432 |
| TabPFNv2-rdkit                     |  0.634    |
| TabPFNv2-rdkit-3D                  |  0.622    |
| CheMeleon                          |  0.606    |

## `tdcommons/pgp-broccatelli`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.901693 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| 1B_MPNN_LargeMix-and-Phenomics     |  0.954    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.942    |
| TabPFNv2-rdkit                     |  0.941    |
| TabPFNv2-rdkit-3D                  |  0.93     |
| CheMeleon                          |  0.911    |
| ChemPFN                            |  0.901693 |
| MHNfs                              |  0.834    |

## `tdcommons/caco2-wang`

### Model Performance
|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 0.31267 |

### Leaderboard Comparison
| Name                                      |   mean_absolute_error |
|:------------------------------------------|----------------------:|
| mini-PlanE-Seed-Descriptor                |               0.27    |
| agentomics-ml-caco2-wang                  |               0.277   |
| 1B_MPNN_MolGPS-ens_LargeMix-and-Phenomics |               0.282   |
| drylab                                    |               0.282   |
| TabPFNv2-maplight_gnn                     |               0.284   |
| TabPFNv2-rdkit                            |               0.285   |
| mini-PlanE-EBasePlanE-ensemble-rich-znorm |               0.301   |
| ChemPFN                                   |               0.31267 |
| mini-PlanE-E-BasePlanE-seed42             |               0.314   |
| 3B_e50_MPNN_LargeMix-and-Phenomics        |               0.316   |
| 1B_MPNN_LargeMix-and-Phenomics            |               0.319   |

## `tdcommons/herg`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.820766 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| agentomics-ml-herg                 |  0.892    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.891    |
| 1B_MPNN_LargeMix-and-Phenomics     |  0.855    |
| TabPFNv2-rdkit                     |  0.849    |
| TabPFNv2-rdkit-3D                  |  0.848    |
| CheMeleon                          |  0.822    |
| ChemPFN                            |  0.820766 |
| 1B_MPNN_LargeMix                   |  0.816    |
| MHNfs                              |  0.671    |

## `tdcommons/bbb-martins`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.871033 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.933    |
| 1B_MPNN_LargeMix-and-Phenomics     |  0.928    |
| TabPFNv2-rdkit-3D                  |  0.919    |
| TabPFNv2-rdkit-3D                  |  0.919    |
| TabPFNv2-rdkit                     |  0.912    |
| TabPFNv2-rdkit                     |  0.91     |
| CheMeleon                          |  0.89     |
| ChemPFN                            |  0.871033 |
| MHNfs                              |  0.616    |

## `tdcommons/ames`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.796141 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| vidraft-ames-ensemble-ref          |  0.877    |
| vidraft-rich-ensemble-ames         |  0.877    |
| vidraft-rich-ensemble-ames         |  0.877    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.868    |
| 1B_MPNN_LargeMix-and-Phenomics     |  0.866    |
| CheMeleon                          |  0.854    |
| TabPFNv2-rdkit-3D                  |  0.847    |
| TabPFNv2-rdkit                     |  0.843    |
| ChemPFN                            |  0.796141 |

## `tdcommons/ld50-zhu`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.607746 |

### Leaderboard Comparison
| Name                               |   mean_absolute_error |
|:-----------------------------------|----------------------:|
| CheMeleon                          |              0.526    |
| TabPFNv2-rdkit                     |              0.6      |
| TabPFNv2-rdkit-3D                  |              0.605    |
| ChemPFN                            |              0.607746 |
| 1B_MPNN_LargeMix-and-Phenomics     |              0.614    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |              0.625    |

# Summary

Average Rank of ChemPFN across benchmarks with 4+ other entries 25: 6.48

results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": {
        "pr_auc": 0.6466479231580687
    },
    "polaris/pkis2-ret-wt-reg-v2": {
        "mean_squared_error": 903.5092150516047
    },
    "polaris/pkis2-kit-wt-cls-v2": {
        "pr_auc": 0.6148336296900969
    },
    "polaris/pkis2-kit-wt-reg-v2": {
        "mean_squared_error": 914.6021650363829
    },
    "polaris/pkis2-egfr-wt-reg-v2": {
        "mean_squared_error": 499.30311246198147
    },
    "polaris/adme-fang-solu-1": {
        "pearsonr": 0.6193190002256952
    },
    "polaris/adme-fang-rppb-1": {
        "pearsonr": 0.8539792587632433
    },
    "polaris/adme-fang-hppb-1": {
        "pearsonr": 0.8282752142154296
    },
    "polaris/adme-fang-perm-1": {
        "pearsonr": 0.7412034614258385
    },
    "polaris/adme-fang-rclint-1": {
        "pearsonr": 0.6333093444673256
    },
    "polaris/adme-fang-hclint-1": {
        "pearsonr": 0.6300777101521496
    },
    "tdcommons/lipophilicity-astrazeneca": {
        "mean_absolute_error": 0.7179333213113605
    },
    "tdcommons/ppbr-az": {
        "mean_absolute_error": 8.677464924438695
    },
    "tdcommons/clearance-hepatocyte-az": {
        "spearmanr": 0.3691557451268476
    },
    "tdcommons/cyp2d6-substrate-carbonmangels": {
        "pr_auc": 0.6070745188674129
    },
    "tdcommons/half-life-obach": {
        "spearmanr": 0.4969560561432797
    },
    "tdcommons/cyp2c9-substrate-carbonmangels": {
        "pr_auc": 0.3952656255918057
    },
    "tdcommons/clearance-microsome-az": {
        "spearmanr": 0.5714827241826638
    },
    "tdcommons/dili": {
        "roc_auc": 0.9369565217391305
    },
    "tdcommons/bioavailability-ma": {
        "roc_auc": 0.6711007648819421
    },
    "tdcommons/vdss-lombardo": {
        "spearmanr": 0.5726013382703775
    },
    "tdcommons/cyp3a4-substrate-carbonmangels": {
        "roc_auc": 0.6374321880650995
    },
    "tdcommons/pgp-broccatelli": {
        "roc_auc": 0.9016928818981605
    },
    "tdcommons/caco2-wang": {
        "mean_absolute_error": 0.31267003593270454
    },
    "tdcommons/herg": {
        "roc_auc": 0.8207658321060383
    },
    "tdcommons/bbb-martins": {
        "roc_auc": 0.8710326766729206
    },
    "tdcommons/ames": {
        "roc_auc": 0.796140515772778
    },
    "tdcommons/ld50-zhu": {
        "mean_absolute_error": 0.6077464168758935
    }
}

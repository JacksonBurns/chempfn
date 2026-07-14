# Eval Results

timestamp: 2026-07-14 11:32:49.346870
reg_checkpoint: reg.ckpt
cls_checkpoint: cls.ckpt

## `polaris/pkis2-ret-wt-cls-v2`

### Model Performance
|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.571429 |
|  1 | test       | CLS_RET        | pr_auc      | 0.678001 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.509638 |
|  3 | test       | CLS_RET        | accuracy    | 0.886792 |
|  4 | test       | CLS_RET        | roc_auc     | 0.814937 |
|  5 | test       | CLS_RET        | mcc         | 0.525683 |

### Leaderboard Comparison
| Name                                 |   pr_auc |
|:-------------------------------------|---------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics   | 0.885    |
| 1B_MolGPS-ens_LargeMix-and-Phenomics | 0.879    |
| ChemPFN                              | 0.678001 |
| CheMeleon                            | 0.639    |
| MHNfs                                | 0.417    |

## `polaris/pkis2-ret-wt-reg-v2`

### Model Performance
|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | mean_absolute_error |  21.9158   |
|  1 | test       | RET            | r2                  |   0.339774 |
|  2 | test       | RET            | spearmanr           |   0.5942   |
|  3 | test       | RET            | pearsonr            |   0.645192 |
|  4 | test       | RET            | explained_var       |   0.358027 |
|  5 | test       | RET            | mean_squared_error  | 783.956    |

### Leaderboard Comparison
| Name                                 |   mean_squared_error |
|:-------------------------------------|---------------------:|
| 1B_MolGPS-ens_LargeMix-and-Phenomics |              589.944 |
| 3B_e50_MPNN_LargeMix-and-Phenomics   |              609.399 |
| CheMeleon                            |              684.319 |
| CheMeleon                            |              724.347 |
| ChemPFN                              |              783.956 |

## `polaris/pkis2-kit-wt-cls-v2`

### Model Performance
|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.566038 |
|  1 | test       | CLS_KIT        | pr_auc      | 0.58873  |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.442308 |
|  3 | test       | CLS_KIT        | accuracy    | 0.801724 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.791103 |
|  5 | test       | CLS_KIT        | mcc         | 0.453232 |

### Leaderboard Comparison
| Name      |   pr_auc |
|:----------|---------:|
| CheMeleon |  0.646   |
| ChemPFN   |  0.58873 |
| MHNfs     |  0.376   |

## `polaris/pkis2-kit-wt-reg-v2`

### Model Performance
|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | mean_absolute_error |  23.1046   |
|  1 | test       | KIT            | r2                  |   0.25091  |
|  2 | test       | KIT            | spearmanr           |   0.474223 |
|  3 | test       | KIT            | pearsonr            |   0.562618 |
|  4 | test       | KIT            | explained_var       |   0.315866 |
|  5 | test       | KIT            | mean_squared_error  | 903.915    |

### Leaderboard Comparison
| Name      |   mean_squared_error |
|:----------|---------------------:|
| CheMeleon |              849.611 |
| ChemPFN   |              903.915 |

## `polaris/pkis2-egfr-wt-reg-v2`

### Model Performance
|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | mean_absolute_error |  17.2023   |
|  1 | test       | EGFR           | r2                  |   0.438933 |
|  2 | test       | EGFR           | spearmanr           |   0.35938  |
|  3 | test       | EGFR           | pearsonr            |   0.676562 |
|  4 | test       | EGFR           | explained_var       |   0.442747 |
|  5 | test       | EGFR           | mean_squared_error  | 452.09     |

### Leaderboard Comparison
| Name                                   |   mean_squared_error |
|:---------------------------------------|---------------------:|
| aether-pharmaos-pkis2-egfr-wt-ensemble |              430.821 |
| ChemPFN                                |              452.09  |
| CheMeleon                              |              459.929 |

## `polaris/adme-fang-solu-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.421339 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.356356 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.497306 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.608473 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.357179 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.34897  |

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
| ChemPFN                     |   0.608473 |

## `polaris/adme-fang-rppb-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | mean_absolute_error | 0.463114 |
|  1 | test       | LOG_RPPB       | r2                  | 0.590481 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.886957 |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.821978 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.609843 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.36385  |

### Leaderboard Comparison
| Name                                          |   pearsonr |
|:----------------------------------------------|-----------:|
| 1B_MPNN_LargeMix-and-Phenomics                |   0.908    |
| 1B_MPNN_MolGPS-ens_LargeMix                   |   0.886    |
| nepare                                        |   0.863    |
| ChemPFN                                       |   0.821978 |
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
|  0 | test       | LOG_HPPB       | mean_absolute_error | 0.428223 |
|  1 | test       | LOG_HPPB       | r2                  | 0.585894 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.811674 |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.80736  |
|  4 | test       | LOG_HPPB       | explained_var       | 0.636756 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.250799 |

### Leaderboard Comparison
| Name                                            |   pearsonr |
|:------------------------------------------------|-----------:|
| 1B_MPNN_LargeMix-and-Phenomics                  |    0.888   |
| 1B_MPNN_MolGPS-ens_LargeMix                     |    0.884   |
| TabPFNv2-rdkit                                  |    0.827   |
| adme-fang-HPPB-1-GIRAFFE-wae                    |    0.815   |
| agentomics-ml-adme-fang-hppb-1                  |    0.815   |
| nepare                                          |    0.809   |
| ChemPFN                                         |    0.80736 |
| CheMeleon                                       |    0.793   |
| chemlactica-125m-sft                            |    0.774   |
| adme-fang-HPPB-1_atompair_RandomForestRegressor |    0.69    |
| chemma-2b-sft                                   |    0.636   |

## `polaris/adme-fang-perm-1`

### Model Performance
|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.379556 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.520523 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.72199  |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.737895 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.52229  |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.23753  |

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
| ChemPFN                                       |   0.737895 |
| optimized-random-forest-rdkit-descriptors     |   0.727    |
| adme-fang-PERM-1_desc2D_RandomForestRegressor |   0.716    |
| chemlactica-125m-sft                          |   0.714    |

## `polaris/adme-fang-rclint-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.470285 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.396565 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.633983 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.635146 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.399567 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.340665 |

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
| ChemPFN                                         |   0.635146 |
| adme-fang-RCLint-1_desc2D_RandomForestRegressor |   0.631    |
| adme-fang-RCLint-1_desc2D_FCModel               |   0.544    |

## `polaris/adme-fang-hclint-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.418875 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.357375 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.599875 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.60262  |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.358655 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.249602 |

### Leaderboard Comparison
| Name                                            |   pearsonr |
|:------------------------------------------------|-----------:|
| seqera-gradient                                 |    0.796   |
| 1B_MPNN_LargeMix-and-Phenomics                  |    0.778   |
| chemlactica-1b-sft                              |    0.72    |
| CheMeleon                                       |    0.72    |
| chemlactica-125m-sft                            |    0.717   |
| MolEncoder                                      |    0.714   |
| agentomics-ml-adme-fang-hclint-1                |    0.697   |
| chemma-2b-sft                                   |    0.674   |
| TabPFNv2-rdkit                                  |    0.662   |
| adme-fang-HCLint-1_desc2D_RandomForestRegressor |    0.639   |
| ChemPFN                                         |    0.60262 |

## `tdcommons/lipophilicity-astrazeneca`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.715713 |

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
| ChemPFN                                   |              0.715713 |

## `tdcommons/ppbr-az`

### Model Performance
|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 9.72209 |

### Leaderboard Comparison
| Name                               |   mean_absolute_error |
|:-----------------------------------|----------------------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics |               7.004   |
| 1B_MPNN_LargeMix-and-Phenomics     |               7.026   |
| TabPFNv2-rdkit-3D                  |               7.033   |
| TabPFNv2-rdkit                     |               7.117   |
| CheMeleon                          |               7.532   |
| ChemPFN                            |               9.72209 |

## `tdcommons/clearance-hepatocyte-az`

### Model Performance
|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.393826 |

### Leaderboard Comparison
| Name                                |   spearmanr |
|:------------------------------------|------------:|
| 1B_MPNN_LargeMix-and-Phenomics      |    0.538    |
| 3B_e50_MPNN_LargeMix-and-Phenomics  |    0.525    |
| clearance-hepatocyte-az-GIRAFFE-wae |    0.429    |
| TabPFNv2-rdkit                      |    0.41     |
| TabPFNv2-rdkit-3D                   |    0.402    |
| ChemPFN                             |    0.393826 |
| CheMeleon                           |    0.387    |

## `tdcommons/cyp2d6-substrate-carbonmangels`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.611627 |

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
| ChemPFN                                      | 0.611627 |
| ARKA-Mordred                                 | 0.558    |

## `tdcommons/half-life-obach`

### Model Performance
|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.468143 |

### Leaderboard Comparison
| Name                               |   spearmanr |
|:-----------------------------------|------------:|
| 1B_MPNN_LargeMix-and-Phenomics     |    0.625    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |    0.573    |
| TabPFNv2-rdkit                     |    0.542    |
| TabPFNv2-rdkit-3D                  |    0.489    |
| ChemPFN                            |    0.468143 |
| MolEncoder                         |    0.417    |
| CheMeleon                          |    0.36     |

## `tdcommons/cyp2c9-substrate-carbonmangels`

### Model Performance
|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | pr_auc   | 0.42246 |

### Leaderboard Comparison
| Name                               |   pr_auc |
|:-----------------------------------|---------:|
| 1B_MPNN_LargeMix-and-Phenomics     |  0.478   |
| CheMeleon                          |  0.47    |
| ChemPFN                            |  0.42246 |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.407   |
| TabPFNv2-rdkit                     |  0.378   |
| MHNfs                              |  0.276   |

## `tdcommons/clearance-microsome-az`

### Model Performance
|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.58647 |

### Leaderboard Comparison
| Name                               |   spearmanr |
|:-----------------------------------|------------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics |     0.683   |
| 1B_MPNN_LargeMix-and-Phenomics     |     0.653   |
| TabPFNv2-rdkit-3D                  |     0.649   |
| TabPFNv2-rdkit                     |     0.64    |
| CheMeleon                          |     0.59    |
| ChemPFN                            |     0.58647 |

## `tdcommons/dili`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.936087 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| ChemPFN                            |  0.936087 |
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
|  0 | test       | Y              | roc_auc  | 0.690389 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| vidraft-tabpfn-ensemble-bioavail   |  0.734    |
| TabPFNv2-rdkit-3D                  |  0.729    |
| TabPFNv2-rdkit                     |  0.728    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.714    |
| CheMeleon                          |  0.698    |
| ChemPFN                            |  0.690389 |
| 1B_MPNN_LargeMix-and-Phenomics     |  0.675    |
| MHNfs                              |  0.61     |

## `tdcommons/vdss-lombardo`

### Model Performance
|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.538133 |

### Leaderboard Comparison
| Name                               |   spearmanr |
|:-----------------------------------|------------:|
| vidraft-tabpfn-vdss                |    0.726    |
| TabPFNv2-rdkit                     |    0.7      |
| TabPFNv2-rdkit-3D                  |    0.69     |
| 1B_MPNN_LargeMix-and-Phenomics     |    0.637    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |    0.6      |
| CheMeleon                          |    0.59     |
| ChemPFN                            |    0.538133 |

## `tdcommons/cyp3a4-substrate-carbonmangels`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.631329 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| 1B_MPNN_LargeMix-and-Phenomics     |  0.696    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.685    |
| TabPFNv2-rdkit                     |  0.634    |
| ChemPFN                            |  0.631329 |
| TabPFNv2-rdkit-3D                  |  0.622    |
| CheMeleon                          |  0.606    |

## `tdcommons/pgp-broccatelli`

### Model Performance
|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.88583 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| 1B_MPNN_LargeMix-and-Phenomics     |   0.954   |
| 3B_e50_MPNN_LargeMix-and-Phenomics |   0.942   |
| TabPFNv2-rdkit                     |   0.941   |
| TabPFNv2-rdkit-3D                  |   0.93    |
| CheMeleon                          |   0.911   |
| ChemPFN                            |   0.88583 |
| MHNfs                              |   0.834   |

## `tdcommons/caco2-wang`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.306583 |

### Leaderboard Comparison
| Name                                      |   mean_absolute_error |
|:------------------------------------------|----------------------:|
| mini-PlanE-Seed-Descriptor                |              0.27     |
| agentomics-ml-caco2-wang                  |              0.277    |
| 1B_MPNN_MolGPS-ens_LargeMix-and-Phenomics |              0.282    |
| drylab                                    |              0.282    |
| TabPFNv2-maplight_gnn                     |              0.284    |
| TabPFNv2-rdkit                            |              0.285    |
| mini-PlanE-EBasePlanE-ensemble-rich-znorm |              0.301    |
| ChemPFN                                   |              0.306583 |
| mini-PlanE-E-BasePlanE-seed42             |              0.314    |
| 3B_e50_MPNN_LargeMix-and-Phenomics        |              0.316    |
| 1B_MPNN_LargeMix-and-Phenomics            |              0.319    |

## `tdcommons/herg`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.817968 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| agentomics-ml-herg                 |  0.892    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.891    |
| 1B_MPNN_LargeMix-and-Phenomics     |  0.855    |
| TabPFNv2-rdkit                     |  0.849    |
| TabPFNv2-rdkit-3D                  |  0.848    |
| CheMeleon                          |  0.822    |
| ChemPFN                            |  0.817968 |
| 1B_MPNN_LargeMix                   |  0.816    |
| MHNfs                              |  0.671    |

## `tdcommons/bbb-martins`

### Model Performance
|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.85659 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics |   0.933   |
| 1B_MPNN_LargeMix-and-Phenomics     |   0.928   |
| TabPFNv2-rdkit-3D                  |   0.919   |
| TabPFNv2-rdkit-3D                  |   0.919   |
| TabPFNv2-rdkit                     |   0.912   |
| TabPFNv2-rdkit                     |   0.91    |
| CheMeleon                          |   0.89    |
| ChemPFN                            |   0.85659 |
| MHNfs                              |   0.616   |

## `tdcommons/ames`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.799285 |

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
| ChemPFN                            |  0.799285 |

## `tdcommons/ld50-zhu`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.616336 |

### Leaderboard Comparison
| Name                               |   mean_absolute_error |
|:-----------------------------------|----------------------:|
| CheMeleon                          |              0.526    |
| TabPFNv2-rdkit                     |              0.6      |
| TabPFNv2-rdkit-3D                  |              0.605    |
| 1B_MPNN_LargeMix-and-Phenomics     |              0.614    |
| ChemPFN                            |              0.616336 |
| 3B_e50_MPNN_LargeMix-and-Phenomics |              0.625    |

# Summary

Average Rank of ChemPFN across benchmarks with 4+ other entries 25: 6.64

results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": {
        "pr_auc": 0.6780008058470601
    },
    "polaris/pkis2-ret-wt-reg-v2": {
        "mean_squared_error": 783.9561613849299
    },
    "polaris/pkis2-kit-wt-cls-v2": {
        "pr_auc": 0.5887296623009375
    },
    "polaris/pkis2-kit-wt-reg-v2": {
        "mean_squared_error": 903.9145818589265
    },
    "polaris/pkis2-egfr-wt-reg-v2": {
        "mean_squared_error": 452.090294439125
    },
    "polaris/adme-fang-solu-1": {
        "pearsonr": 0.6084731924196005
    },
    "polaris/adme-fang-rppb-1": {
        "pearsonr": 0.821977939788457
    },
    "polaris/adme-fang-hppb-1": {
        "pearsonr": 0.8073597530491922
    },
    "polaris/adme-fang-perm-1": {
        "pearsonr": 0.7378953448300322
    },
    "polaris/adme-fang-rclint-1": {
        "pearsonr": 0.6351460199534651
    },
    "polaris/adme-fang-hclint-1": {
        "pearsonr": 0.6026198744405276
    },
    "tdcommons/lipophilicity-astrazeneca": {
        "mean_absolute_error": 0.7157125450599761
    },
    "tdcommons/ppbr-az": {
        "mean_absolute_error": 9.722088184117844
    },
    "tdcommons/clearance-hepatocyte-az": {
        "spearmanr": 0.3938257231810172
    },
    "tdcommons/cyp2d6-substrate-carbonmangels": {
        "pr_auc": 0.6116272597511295
    },
    "tdcommons/half-life-obach": {
        "spearmanr": 0.4681427905123778
    },
    "tdcommons/cyp2c9-substrate-carbonmangels": {
        "pr_auc": 0.4224604793054124
    },
    "tdcommons/clearance-microsome-az": {
        "spearmanr": 0.5864700004953058
    },
    "tdcommons/dili": {
        "roc_auc": 0.9360869565217391
    },
    "tdcommons/bioavailability-ma": {
        "roc_auc": 0.6903890921183904
    },
    "tdcommons/vdss-lombardo": {
        "spearmanr": 0.5381330598656113
    },
    "tdcommons/cyp3a4-substrate-carbonmangels": {
        "roc_auc": 0.6313291139240506
    },
    "tdcommons/pgp-broccatelli": {
        "roc_auc": 0.8858304452146094
    },
    "tdcommons/caco2-wang": {
        "mean_absolute_error": 0.3065833979511304
    },
    "tdcommons/herg": {
        "roc_auc": 0.8179675994108985
    },
    "tdcommons/bbb-martins": {
        "roc_auc": 0.8565900562851783
    },
    "tdcommons/ames": {
        "roc_auc": 0.7992852806986626
    },
    "tdcommons/ld50-zhu": {
        "mean_absolute_error": 0.6163359693932438
    }
}

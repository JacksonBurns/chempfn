# Eval Results

timestamp: 2026-07-28 09:44:33.888075
reg_checkpoint: /home/jwburns/chempfn/logs/regression/lightning_logs/version_6/checkpoints/model-epoch=782-train_loss_epoch=4.2842.ckpt
cls_checkpoint: /home/jwburns/chempfn/logs/classification/lightning_logs/version_5/checkpoints/model-epoch=170-train_loss_epoch=0.4688.ckpt

## `polaris/pkis2-ret-wt-cls-v2`

### Model Performance
|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | f1          | 0.538462 |
|  1 | test       | CLS_RET        | accuracy    | 0.886792 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.480816 |
|  3 | test       | CLS_RET        | mcc         | 0.512494 |
|  4 | test       | CLS_RET        | pr_auc      | 0.681175 |
|  5 | test       | CLS_RET        | roc_auc     | 0.869134 |

### Leaderboard Comparison
| Name                                 |   pr_auc |
|:-------------------------------------|---------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics   | 0.885    |
| 1B_MolGPS-ens_LargeMix-and-Phenomics | 0.879    |
| ChemPFN                              | 0.681175 |
| CheMeleon                            | 0.639    |
| MHNfs                                | 0.417    |

## `polaris/pkis2-ret-wt-reg-v2`

### Model Performance
|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | r2                  |   0.225247 |
|  1 | test       | RET            | mean_absolute_error |  24.4164   |
|  2 | test       | RET            | spearmanr           |   0.485823 |
|  3 | test       | RET            | pearsonr            |   0.581341 |
|  4 | test       | RET            | explained_var       |   0.23929  |
|  5 | test       | RET            | mean_squared_error  | 919.945    |

### Leaderboard Comparison
| Name                                 |   mean_squared_error |
|:-------------------------------------|---------------------:|
| 1B_MolGPS-ens_LargeMix-and-Phenomics |              589.944 |
| 3B_e50_MPNN_LargeMix-and-Phenomics   |              609.399 |
| CheMeleon                            |              684.319 |
| CheMeleon                            |              724.347 |
| ChemPFN                              |              919.945 |

## `polaris/pkis2-kit-wt-cls-v2`

### Model Performance
|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | f1          | 0.631579 |
|  1 | test       | CLS_KIT        | accuracy    | 0.818966 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.519716 |
|  3 | test       | CLS_KIT        | mcc         | 0.544332 |
|  4 | test       | CLS_KIT        | pr_auc      | 0.50854  |
|  5 | test       | CLS_KIT        | roc_auc     | 0.777079 |

### Leaderboard Comparison
| Name      |   pr_auc |
|:----------|---------:|
| CheMeleon |  0.646   |
| ChemPFN   |  0.50854 |
| MHNfs     |  0.376   |

## `polaris/pkis2-kit-wt-reg-v2`

### Model Performance
|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | r2                  |   0.280135 |
|  1 | test       | KIT            | mean_absolute_error |  24.8958   |
|  2 | test       | KIT            | spearmanr           |   0.446396 |
|  3 | test       | KIT            | pearsonr            |   0.53103  |
|  4 | test       | KIT            | explained_var       |   0.280315 |
|  5 | test       | KIT            | mean_squared_error  | 868.649    |

### Leaderboard Comparison
| Name      |   mean_squared_error |
|:----------|---------------------:|
| CheMeleon |              849.611 |
| ChemPFN   |              868.649 |

## `polaris/pkis2-egfr-wt-reg-v2`

### Model Performance
|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | r2                  |   0.262349 |
|  1 | test       | EGFR           | mean_absolute_error |  19.4438   |
|  2 | test       | EGFR           | spearmanr           |   0.269795 |
|  3 | test       | EGFR           | pearsonr            |   0.599123 |
|  4 | test       | EGFR           | explained_var       |   0.263945 |
|  5 | test       | EGFR           | mean_squared_error  | 594.376    |

### Leaderboard Comparison
| Name                                   |   mean_squared_error |
|:---------------------------------------|---------------------:|
| aether-pharmaos-pkis2-egfr-wt-ensemble |              430.821 |
| CheMeleon                              |              459.929 |
| ChemPFN                                |              594.376 |

## `polaris/adme-fang-solu-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | r2                  | 0.325333 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.410979 |
|  2 | test       | LOG_SOLUBILITY | spearmanr           | 0.506379 |
|  3 | test       | LOG_SOLUBILITY | pearsonr            | 0.606095 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.333851 |
|  5 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.36579  |

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
| ChemPFN                     |   0.606095 |

## `polaris/adme-fang-rppb-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | r2                  | 0.423116 |
|  1 | test       | LOG_RPPB       | mean_absolute_error | 0.591465 |
|  2 | test       | LOG_RPPB       | spearmanr           | 0.866087 |
|  3 | test       | LOG_RPPB       | pearsonr            | 0.791998 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.444302 |
|  5 | test       | LOG_RPPB       | mean_squared_error  | 0.512551 |

### Leaderboard Comparison
| Name                                          |   pearsonr |
|:----------------------------------------------|-----------:|
| 1B_MPNN_LargeMix-and-Phenomics                |   0.908    |
| 1B_MPNN_MolGPS-ens_LargeMix                   |   0.886    |
| nepare                                        |   0.863    |
| TabPFNv2-rdkit                                |   0.816    |
| ChemPFN                                       |   0.791998 |
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
|  0 | test       | LOG_HPPB       | r2                  | 0.550299 |
|  1 | test       | LOG_HPPB       | mean_absolute_error | 0.439571 |
|  2 | test       | LOG_HPPB       | spearmanr           | 0.772252 |
|  3 | test       | LOG_HPPB       | pearsonr            | 0.78056  |
|  4 | test       | LOG_HPPB       | explained_var       | 0.568278 |
|  5 | test       | LOG_HPPB       | mean_squared_error  | 0.272356 |

### Leaderboard Comparison
| Name                                            |   pearsonr |
|:------------------------------------------------|-----------:|
| 1B_MPNN_LargeMix-and-Phenomics                  |    0.888   |
| 1B_MPNN_MolGPS-ens_LargeMix                     |    0.884   |
| TabPFNv2-rdkit                                  |    0.827   |
| adme-fang-HPPB-1-GIRAFFE-wae                    |    0.815   |
| agentomics-ml-adme-fang-hppb-1                  |    0.815   |
| nepare                                          |    0.809   |
| CheMeleon                                       |    0.793   |
| ChemPFN                                         |    0.78056 |
| chemlactica-125m-sft                            |    0.774   |
| adme-fang-HPPB-1_atompair_RandomForestRegressor |    0.69    |
| chemma-2b-sft                                   |    0.636   |

## `polaris/adme-fang-perm-1`

### Model Performance
|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.519397 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.366705 |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.735304 |
|  3 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.742655 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.523753 |
|  5 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.238087 |

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
| ChemPFN                                       |   0.742655 |
| optimized-random-forest-rdkit-descriptors     |   0.727    |
| adme-fang-PERM-1_desc2D_RandomForestRegressor |   0.716    |
| chemlactica-125m-sft                          |   0.714    |

## `polaris/adme-fang-rclint-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | r2                  | 0.368242 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.489619 |
|  2 | test       | LOG_RLM_CLint  | spearmanr           | 0.620748 |
|  3 | test       | LOG_RLM_CLint  | pearsonr            | 0.626712 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.368379 |
|  5 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.356655 |

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
| adme-fang-RCLint-1_desc2D_RandomForestRegressor |   0.631    |
| ChemPFN                                         |   0.626712 |
| adme-fang-RCLint-1_desc2D_FCModel               |   0.544    |

## `polaris/adme-fang-hclint-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | r2                  | 0.240604 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.456145 |
|  2 | test       | LOG_HLM_CLint  | spearmanr           | 0.563318 |
|  3 | test       | LOG_HLM_CLint  | pearsonr            | 0.569029 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.248444 |
|  5 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.294957 |

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
| ChemPFN                                         |   0.569029 |

## `tdcommons/lipophilicity-astrazeneca`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.756256 |

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
| ChemPFN                                   |              0.756256 |

## `tdcommons/ppbr-az`

### Model Performance
|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.27241 |

### Leaderboard Comparison
| Name                               |   mean_absolute_error |
|:-----------------------------------|----------------------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics |               7.004   |
| 1B_MPNN_LargeMix-and-Phenomics     |               7.026   |
| TabPFNv2-rdkit-3D                  |               7.033   |
| TabPFNv2-rdkit                     |               7.117   |
| CheMeleon                          |               7.532   |
| ChemPFN                            |               8.27241 |

## `tdcommons/clearance-hepatocyte-az`

### Model Performance
|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.369522 |

### Leaderboard Comparison
| Name                                |   spearmanr |
|:------------------------------------|------------:|
| 1B_MPNN_LargeMix-and-Phenomics      |    0.538    |
| 3B_e50_MPNN_LargeMix-and-Phenomics  |    0.525    |
| clearance-hepatocyte-az-GIRAFFE-wae |    0.429    |
| TabPFNv2-rdkit                      |    0.41     |
| TabPFNv2-rdkit-3D                   |    0.402    |
| CheMeleon                           |    0.387    |
| ChemPFN                             |    0.369522 |

## `tdcommons/cyp2d6-substrate-carbonmangels`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.613897 |

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
| ChemPFN                                      | 0.613897 |
| ARKA-Mordred                                 | 0.558    |

## `tdcommons/half-life-obach`

### Model Performance
|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.463319 |

### Leaderboard Comparison
| Name                               |   spearmanr |
|:-----------------------------------|------------:|
| 1B_MPNN_LargeMix-and-Phenomics     |    0.625    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |    0.573    |
| TabPFNv2-rdkit                     |    0.542    |
| TabPFNv2-rdkit-3D                  |    0.489    |
| ChemPFN                            |    0.463319 |
| MolEncoder                         |    0.417    |
| CheMeleon                          |    0.36     |

## `tdcommons/cyp2c9-substrate-carbonmangels`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.451597 |

### Leaderboard Comparison
| Name                               |   pr_auc |
|:-----------------------------------|---------:|
| 1B_MPNN_LargeMix-and-Phenomics     | 0.478    |
| CheMeleon                          | 0.47     |
| ChemPFN                            | 0.451597 |
| 3B_e50_MPNN_LargeMix-and-Phenomics | 0.407    |
| TabPFNv2-rdkit                     | 0.378    |
| MHNfs                              | 0.276    |

## `tdcommons/clearance-microsome-az`

### Model Performance
|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.556564 |

### Leaderboard Comparison
| Name                               |   spearmanr |
|:-----------------------------------|------------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics |    0.683    |
| 1B_MPNN_LargeMix-and-Phenomics     |    0.653    |
| TabPFNv2-rdkit-3D                  |    0.649    |
| TabPFNv2-rdkit                     |    0.64     |
| CheMeleon                          |    0.59     |
| ChemPFN                            |    0.556564 |

## `tdcommons/dili`

### Model Performance
|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.93087 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| vidraft-structure-ensemble-dili    |   0.933   |
| 3B_e50_MPNN_LargeMix-and-Phenomics |   0.933   |
| ChemPFN                            |   0.93087 |
| TabPFNv2-rdkit-3D                  |   0.93    |
| 1B_MPNN_LargeMix-and-Phenomics     |   0.925   |
| CheMeleon                          |   0.916   |
| TabPFNv2-rdkit                     |   0.9     |

## `tdcommons/bioavailability-ma`

### Model Performance
|    | Test set   | Target label   | Metric   |   Score |
|---:|:-----------|:---------------|:---------|--------:|
|  0 | test       | Y              | roc_auc  | 0.68008 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| vidraft-tabpfn-ensemble-bioavail   |   0.734   |
| TabPFNv2-rdkit-3D                  |   0.729   |
| TabPFNv2-rdkit                     |   0.728   |
| 3B_e50_MPNN_LargeMix-and-Phenomics |   0.714   |
| CheMeleon                          |   0.698   |
| ChemPFN                            |   0.68008 |
| 1B_MPNN_LargeMix-and-Phenomics     |   0.675   |
| MHNfs                              |   0.61    |

## `tdcommons/vdss-lombardo`

### Model Performance
|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.630435 |

### Leaderboard Comparison
| Name                               |   spearmanr |
|:-----------------------------------|------------:|
| vidraft-tabpfn-vdss                |    0.726    |
| TabPFNv2-rdkit                     |    0.7      |
| TabPFNv2-rdkit-3D                  |    0.69     |
| 1B_MPNN_LargeMix-and-Phenomics     |    0.637    |
| ChemPFN                            |    0.630435 |
| 3B_e50_MPNN_LargeMix-and-Phenomics |    0.6      |
| CheMeleon                          |    0.59     |

## `tdcommons/cyp3a4-substrate-carbonmangels`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.646248 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| 1B_MPNN_LargeMix-and-Phenomics     |  0.696    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.685    |
| ChemPFN                            |  0.646248 |
| TabPFNv2-rdkit                     |  0.634    |
| TabPFNv2-rdkit-3D                  |  0.622    |
| CheMeleon                          |  0.606    |

## `tdcommons/pgp-broccatelli`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.893562 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| 1B_MPNN_LargeMix-and-Phenomics     |  0.954    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.942    |
| TabPFNv2-rdkit                     |  0.941    |
| TabPFNv2-rdkit-3D                  |  0.93     |
| CheMeleon                          |  0.911    |
| ChemPFN                            |  0.893562 |
| MHNfs                              |  0.834    |

## `tdcommons/caco2-wang`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.347979 |

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
| mini-PlanE-E-BasePlanE-seed42             |              0.314    |
| 3B_e50_MPNN_LargeMix-and-Phenomics        |              0.316    |
| 1B_MPNN_LargeMix-and-Phenomics            |              0.319    |
| ChemPFN                                   |              0.347979 |

## `tdcommons/herg`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.830191 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| agentomics-ml-herg                 |  0.892    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.891    |
| 1B_MPNN_LargeMix-and-Phenomics     |  0.855    |
| TabPFNv2-rdkit                     |  0.849    |
| TabPFNv2-rdkit-3D                  |  0.848    |
| ChemPFN                            |  0.830191 |
| CheMeleon                          |  0.822    |
| 1B_MPNN_LargeMix                   |  0.816    |
| MHNfs                              |  0.671    |

## `tdcommons/bbb-martins`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.858662 |

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
| ChemPFN                            |  0.858662 |
| MHNfs                              |  0.616    |

## `tdcommons/ames`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.801665 |

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
| ChemPFN                            |  0.801665 |

## `tdcommons/ld50-zhu`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.688018 |

### Leaderboard Comparison
| Name                               |   mean_absolute_error |
|:-----------------------------------|----------------------:|
| CheMeleon                          |              0.526    |
| TabPFNv2-rdkit                     |              0.6      |
| TabPFNv2-rdkit-3D                  |              0.605    |
| 1B_MPNN_LargeMix-and-Phenomics     |              0.614    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |              0.625    |
| ChemPFN                            |              0.688018 |

# Summary

Average Rank of ChemPFN across benchmarks with 4+ other entries 25: 6.88

results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": {
        "pr_auc": 0.6811750443377858
    },
    "polaris/pkis2-ret-wt-reg-v2": {
        "mean_squared_error": 919.9454080605403
    },
    "polaris/pkis2-kit-wt-cls-v2": {
        "pr_auc": 0.5085395475376665
    },
    "polaris/pkis2-kit-wt-reg-v2": {
        "mean_squared_error": 868.6490905261959
    },
    "polaris/pkis2-egfr-wt-reg-v2": {
        "mean_squared_error": 594.3763026323945
    },
    "polaris/adme-fang-solu-1": {
        "pearsonr": 0.606094801526689
    },
    "polaris/adme-fang-rppb-1": {
        "pearsonr": 0.7919979903309785
    },
    "polaris/adme-fang-hppb-1": {
        "pearsonr": 0.7805604707040441
    },
    "polaris/adme-fang-perm-1": {
        "pearsonr": 0.7426551006441025
    },
    "polaris/adme-fang-rclint-1": {
        "pearsonr": 0.6267116664292584
    },
    "polaris/adme-fang-hclint-1": {
        "pearsonr": 0.5690287699059836
    },
    "tdcommons/lipophilicity-astrazeneca": {
        "mean_absolute_error": 0.7562559010656108
    },
    "tdcommons/ppbr-az": {
        "mean_absolute_error": 8.272406088840983
    },
    "tdcommons/clearance-hepatocyte-az": {
        "spearmanr": 0.36952187620122817
    },
    "tdcommons/cyp2d6-substrate-carbonmangels": {
        "pr_auc": 0.6138968887130195
    },
    "tdcommons/half-life-obach": {
        "spearmanr": 0.46331897831579605
    },
    "tdcommons/cyp2c9-substrate-carbonmangels": {
        "pr_auc": 0.45159737167273517
    },
    "tdcommons/clearance-microsome-az": {
        "spearmanr": 0.5565636209171965
    },
    "tdcommons/dili": {
        "roc_auc": 0.9308695652173914
    },
    "tdcommons/bioavailability-ma": {
        "roc_auc": 0.6800798137678749
    },
    "tdcommons/vdss-lombardo": {
        "spearmanr": 0.6304352821686097
    },
    "tdcommons/cyp3a4-substrate-carbonmangels": {
        "roc_auc": 0.64624773960217
    },
    "tdcommons/pgp-broccatelli": {
        "roc_auc": 0.8935617168754998
    },
    "tdcommons/caco2-wang": {
        "mean_absolute_error": 0.3479790712963398
    },
    "tdcommons/herg": {
        "roc_auc": 0.8301914580265095
    },
    "tdcommons/bbb-martins": {
        "roc_auc": 0.8586616635397124
    },
    "tdcommons/ames": {
        "roc_auc": 0.8016653938788698
    },
    "tdcommons/ld50-zhu": {
        "mean_absolute_error": 0.6880181814033705
    }
}

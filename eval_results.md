# Eval Results

timestamp: 2026-07-20 12:44:16.455544
reg_checkpoint: reg.ckpt
cls_checkpoint: cls.ckpt

## `polaris/pkis2-ret-wt-cls-v2`

### Model Performance
|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | mcc         | 0.512494 |
|  1 | test       | CLS_RET        | f1          | 0.538462 |
|  2 | test       | CLS_RET        | pr_auc      | 0.598231 |
|  3 | test       | CLS_RET        | roc_auc     | 0.829478 |
|  4 | test       | CLS_RET        | accuracy    | 0.886792 |
|  5 | test       | CLS_RET        | cohen_kappa | 0.480816 |

### Leaderboard Comparison
| Name                                 |   pr_auc |
|:-------------------------------------|---------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics   | 0.885    |
| 1B_MolGPS-ens_LargeMix-and-Phenomics | 0.879    |
| CheMeleon                            | 0.639    |
| ChemPFN                              | 0.598231 |
| MHNfs                                | 0.417    |

## `polaris/pkis2-ret-wt-reg-v2`

### Model Performance
|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | RET            | spearmanr           |    0.498991 |
|  1 | test       | RET            | r2                  |    0.115108 |
|  2 | test       | RET            | mean_squared_error  | 1050.73     |
|  3 | test       | RET            | mean_absolute_error |   25.3432   |
|  4 | test       | RET            | explained_var       |    0.14864  |
|  5 | test       | RET            | pearsonr            |    0.577666 |

### Leaderboard Comparison
| Name                                 |   mean_squared_error |
|:-------------------------------------|---------------------:|
| 1B_MolGPS-ens_LargeMix-and-Phenomics |              589.944 |
| 3B_e50_MPNN_LargeMix-and-Phenomics   |              609.399 |
| CheMeleon                            |              684.319 |
| CheMeleon                            |              724.347 |
| ChemPFN                              |             1050.73  |

## `polaris/pkis2-kit-wt-cls-v2`

### Model Performance
|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | mcc         | 0.548632 |
|  1 | test       | CLS_KIT        | f1          | 0.638298 |
|  2 | test       | CLS_KIT        | pr_auc      | 0.626446 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.795938 |
|  4 | test       | CLS_KIT        | accuracy    | 0.853448 |
|  5 | test       | CLS_KIT        | cohen_kappa | 0.546875 |

### Leaderboard Comparison
| Name      |   pr_auc |
|:----------|---------:|
| CheMeleon | 0.646    |
| ChemPFN   | 0.626446 |
| MHNfs     | 0.376    |

## `polaris/pkis2-kit-wt-reg-v2`

### Model Performance
|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.442953 |
|  1 | test       | KIT            | r2                  |   0.23425  |
|  2 | test       | KIT            | mean_squared_error  | 924.018    |
|  3 | test       | KIT            | mean_absolute_error |  25.4742   |
|  4 | test       | KIT            | explained_var       |   0.236381 |
|  5 | test       | KIT            | pearsonr            |   0.487936 |

### Leaderboard Comparison
| Name      |   mean_squared_error |
|:----------|---------------------:|
| CheMeleon |              849.611 |
| ChemPFN   |              924.018 |

## `polaris/pkis2-egfr-wt-reg-v2`

### Model Performance
|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.256865 |
|  1 | test       | EGFR           | r2                  |   0.216782 |
|  2 | test       | EGFR           | mean_squared_error  | 631.092    |
|  3 | test       | EGFR           | mean_absolute_error |  19.4463   |
|  4 | test       | EGFR           | explained_var       |   0.217576 |
|  5 | test       | EGFR           | pearsonr            |   0.579716 |

### Leaderboard Comparison
| Name                                   |   mean_squared_error |
|:---------------------------------------|---------------------:|
| aether-pharmaos-pkis2-egfr-wt-ensemble |              430.821 |
| CheMeleon                              |              459.929 |
| ChemPFN                                |              631.092 |

## `polaris/adme-fang-solu-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.490299 |
|  1 | test       | LOG_SOLUBILITY | r2                  | 0.335937 |
|  2 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.360041 |
|  3 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.403317 |
|  4 | test       | LOG_SOLUBILITY | explained_var       | 0.343695 |
|  5 | test       | LOG_SOLUBILITY | pearsonr            | 0.60193  |

### Leaderboard Comparison
| Name                        |   pearsonr |
|:----------------------------|-----------:|
| 1B_MPNN_MolGPS-ens_LargeMix |    0.77    |
| 1B_MPNN_LargeMix-Phenomics  |    0.764   |
| CheMeleonMOE                |    0.729   |
| CheMeleon                   |    0.682   |
| it-works-now                |    0.669   |
| ML4DD-team16                |    0.654   |
| ML4DD-team9                 |    0.651   |
| team9_submission_2          |    0.651   |
| ExactTanimotoGP             |    0.635   |
| ML4DD-team25                |    0.632   |
| ChemPFN                     |    0.60193 |

## `polaris/adme-fang-rppb-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.871304 |
|  1 | test       | LOG_RPPB       | r2                  | 0.461646 |
|  2 | test       | LOG_RPPB       | mean_squared_error  | 0.478318 |
|  3 | test       | LOG_RPPB       | mean_absolute_error | 0.556782 |
|  4 | test       | LOG_RPPB       | explained_var       | 0.507916 |
|  5 | test       | LOG_RPPB       | pearsonr            | 0.760196 |

### Leaderboard Comparison
| Name                                          |   pearsonr |
|:----------------------------------------------|-----------:|
| 1B_MPNN_LargeMix-and-Phenomics                |   0.908    |
| 1B_MPNN_MolGPS-ens_LargeMix                   |   0.886    |
| nepare                                        |   0.863    |
| TabPFNv2-rdkit                                |   0.816    |
| nepare_chemprop                               |   0.78     |
| ChemPFN                                       |   0.760196 |
| chemma-2b-sft                                 |   0.747    |
| adme-fang-RPPB-1_desc2D_RandomForestRegressor |   0.722    |
| adme-fang-RPPB-1-GIRAFFE-wae                  |   0.68     |
| CheMeleon                                     |   0.662    |
| chemlactica-1b-sft                            |   0.614    |

## `polaris/adme-fang-hppb-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HPPB       | spearmanr           | 0.751776 |
|  1 | test       | LOG_HPPB       | r2                  | 0.546031 |
|  2 | test       | LOG_HPPB       | mean_squared_error  | 0.274941 |
|  3 | test       | LOG_HPPB       | mean_absolute_error | 0.438034 |
|  4 | test       | LOG_HPPB       | explained_var       | 0.570345 |
|  5 | test       | LOG_HPPB       | pearsonr            | 0.768948 |

### Leaderboard Comparison
| Name                                            |   pearsonr |
|:------------------------------------------------|-----------:|
| 1B_MPNN_LargeMix-and-Phenomics                  |   0.888    |
| 1B_MPNN_MolGPS-ens_LargeMix                     |   0.884    |
| TabPFNv2-rdkit                                  |   0.827    |
| adme-fang-HPPB-1-GIRAFFE-wae                    |   0.815    |
| agentomics-ml-adme-fang-hppb-1                  |   0.815    |
| nepare                                          |   0.809    |
| CheMeleon                                       |   0.793    |
| chemlactica-125m-sft                            |   0.774    |
| ChemPFN                                         |   0.768948 |
| adme-fang-HPPB-1_atompair_RandomForestRegressor |   0.69     |
| chemma-2b-sft                                   |   0.636    |

## `polaris/adme-fang-perm-1`

### Model Performance
|    | Test set   | Target label     | Metric              |    Score |
|---:|:-----------|:-----------------|:--------------------|---------:|
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.720434 |
|  1 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.498834 |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.248274 |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.381855 |
|  4 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.499958 |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.728274 |

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
| ChemPFN                                       |   0.728274 |
| optimized-random-forest-rdkit-descriptors     |   0.727    |
| adme-fang-PERM-1_desc2D_RandomForestRegressor |   0.716    |
| chemlactica-125m-sft                          |   0.714    |

## `polaris/adme-fang-rclint-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.606326 |
|  1 | test       | LOG_RLM_CLint  | r2                  | 0.350383 |
|  2 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.366737 |
|  3 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.496865 |
|  4 | test       | LOG_RLM_CLint  | explained_var       | 0.350654 |
|  5 | test       | LOG_RLM_CLint  | pearsonr            | 0.609046 |

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
| ChemPFN                                         |   0.609046 |
| adme-fang-RCLint-1_desc2D_FCModel               |   0.544    |

## `polaris/adme-fang-hclint-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.545249 |
|  1 | test       | LOG_HLM_CLint  | r2                  | 0.236093 |
|  2 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.296709 |
|  3 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.457756 |
|  4 | test       | LOG_HLM_CLint  | explained_var       | 0.239819 |
|  5 | test       | LOG_HLM_CLint  | pearsonr            | 0.546247 |

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
| ChemPFN                                         |   0.546247 |

## `tdcommons/lipophilicity-astrazeneca`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.792531 |

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
| ChemPFN                                   |              0.792531 |

## `tdcommons/ppbr-az`

### Model Performance
|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 8.37069 |

### Leaderboard Comparison
| Name                               |   mean_absolute_error |
|:-----------------------------------|----------------------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics |               7.004   |
| 1B_MPNN_LargeMix-and-Phenomics     |               7.026   |
| TabPFNv2-rdkit-3D                  |               7.033   |
| TabPFNv2-rdkit                     |               7.117   |
| CheMeleon                          |               7.532   |
| ChemPFN                            |               8.37069 |

## `tdcommons/clearance-hepatocyte-az`

### Model Performance
|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.37201 |

### Leaderboard Comparison
| Name                                |   spearmanr |
|:------------------------------------|------------:|
| 1B_MPNN_LargeMix-and-Phenomics      |     0.538   |
| 3B_e50_MPNN_LargeMix-and-Phenomics  |     0.525   |
| clearance-hepatocyte-az-GIRAFFE-wae |     0.429   |
| TabPFNv2-rdkit                      |     0.41    |
| TabPFNv2-rdkit-3D                   |     0.402   |
| CheMeleon                           |     0.387   |
| ChemPFN                             |     0.37201 |

## `tdcommons/cyp2d6-substrate-carbonmangels`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.625707 |

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
| ChemPFN                                      | 0.625707 |
| ARKA-Mordred                                 | 0.558    |

## `tdcommons/half-life-obach`

### Model Performance
|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.499095 |

### Leaderboard Comparison
| Name                               |   spearmanr |
|:-----------------------------------|------------:|
| 1B_MPNN_LargeMix-and-Phenomics     |    0.625    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |    0.573    |
| TabPFNv2-rdkit                     |    0.542    |
| ChemPFN                            |    0.499095 |
| TabPFNv2-rdkit-3D                  |    0.489    |
| MolEncoder                         |    0.417    |
| CheMeleon                          |    0.36     |

## `tdcommons/cyp2c9-substrate-carbonmangels`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.416675 |

### Leaderboard Comparison
| Name                               |   pr_auc |
|:-----------------------------------|---------:|
| 1B_MPNN_LargeMix-and-Phenomics     | 0.478    |
| CheMeleon                          | 0.47     |
| ChemPFN                            | 0.416675 |
| 3B_e50_MPNN_LargeMix-and-Phenomics | 0.407    |
| TabPFNv2-rdkit                     | 0.378    |
| MHNfs                              | 0.276    |

## `tdcommons/clearance-microsome-az`

### Model Performance
|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.558387 |

### Leaderboard Comparison
| Name                               |   spearmanr |
|:-----------------------------------|------------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics |    0.683    |
| 1B_MPNN_LargeMix-and-Phenomics     |    0.653    |
| TabPFNv2-rdkit-3D                  |    0.649    |
| TabPFNv2-rdkit                     |    0.64     |
| CheMeleon                          |    0.59     |
| ChemPFN                            |    0.558387 |

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
|  0 | test       | Y              | roc_auc  | 0.643166 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| vidraft-tabpfn-ensemble-bioavail   |  0.734    |
| TabPFNv2-rdkit-3D                  |  0.729    |
| TabPFNv2-rdkit                     |  0.728    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.714    |
| CheMeleon                          |  0.698    |
| 1B_MPNN_LargeMix-and-Phenomics     |  0.675    |
| ChemPFN                            |  0.643166 |
| MHNfs                              |  0.61     |

## `tdcommons/vdss-lombardo`

### Model Performance
|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.589095 |

### Leaderboard Comparison
| Name                               |   spearmanr |
|:-----------------------------------|------------:|
| vidraft-tabpfn-vdss                |    0.726    |
| TabPFNv2-rdkit                     |    0.7      |
| TabPFNv2-rdkit-3D                  |    0.69     |
| 1B_MPNN_LargeMix-and-Phenomics     |    0.637    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |    0.6      |
| CheMeleon                          |    0.59     |
| ChemPFN                            |    0.589095 |

## `tdcommons/cyp3a4-substrate-carbonmangels`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.642179 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| 1B_MPNN_LargeMix-and-Phenomics     |  0.696    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.685    |
| ChemPFN                            |  0.642179 |
| TabPFNv2-rdkit                     |  0.634    |
| TabPFNv2-rdkit-3D                  |  0.622    |
| CheMeleon                          |  0.606    |

## `tdcommons/pgp-broccatelli`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.904825 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| 1B_MPNN_LargeMix-and-Phenomics     |  0.954    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.942    |
| TabPFNv2-rdkit                     |  0.941    |
| TabPFNv2-rdkit-3D                  |  0.93     |
| CheMeleon                          |  0.911    |
| ChemPFN                            |  0.904825 |
| MHNfs                              |  0.834    |

## `tdcommons/caco2-wang`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.312071 |

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
| ChemPFN                                   |              0.312071 |
| mini-PlanE-E-BasePlanE-seed42             |              0.314    |
| 3B_e50_MPNN_LargeMix-and-Phenomics        |              0.316    |
| 1B_MPNN_LargeMix-and-Phenomics            |              0.319    |

## `tdcommons/herg`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.813108 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| agentomics-ml-herg                 |  0.892    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.891    |
| 1B_MPNN_LargeMix-and-Phenomics     |  0.855    |
| TabPFNv2-rdkit                     |  0.849    |
| TabPFNv2-rdkit-3D                  |  0.848    |
| CheMeleon                          |  0.822    |
| 1B_MPNN_LargeMix                   |  0.816    |
| ChemPFN                            |  0.813108 |
| MHNfs                              |  0.671    |

## `tdcommons/bbb-martins`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.849496 |

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
| ChemPFN                            |  0.849496 |
| MHNfs                              |  0.616    |

## `tdcommons/ames`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.763221 |

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
| ChemPFN                            |  0.763221 |

## `tdcommons/ld50-zhu`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.683486 |

### Leaderboard Comparison
| Name                               |   mean_absolute_error |
|:-----------------------------------|----------------------:|
| CheMeleon                          |              0.526    |
| TabPFNv2-rdkit                     |              0.6      |
| TabPFNv2-rdkit-3D                  |              0.605    |
| 1B_MPNN_LargeMix-and-Phenomics     |              0.614    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |              0.625    |
| ChemPFN                            |              0.683486 |

# Summary

Average Rank of ChemPFN across benchmarks with 4+ other entries 25: 6.96

results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": {
        "pr_auc": 0.5982309184001295
    },
    "polaris/pkis2-ret-wt-reg-v2": {
        "mean_squared_error": 1050.7255723892586
    },
    "polaris/pkis2-kit-wt-cls-v2": {
        "pr_auc": 0.6264455375224824
    },
    "polaris/pkis2-kit-wt-reg-v2": {
        "mean_squared_error": 924.0182605686277
    },
    "polaris/pkis2-egfr-wt-reg-v2": {
        "mean_squared_error": 631.0923511903494
    },
    "polaris/adme-fang-solu-1": {
        "pearsonr": 0.6019298446027839
    },
    "polaris/adme-fang-rppb-1": {
        "pearsonr": 0.7601955536283735
    },
    "polaris/adme-fang-hppb-1": {
        "pearsonr": 0.7689479372296383
    },
    "polaris/adme-fang-perm-1": {
        "pearsonr": 0.7282740174162076
    },
    "polaris/adme-fang-rclint-1": {
        "pearsonr": 0.6090459021767767
    },
    "polaris/adme-fang-hclint-1": {
        "pearsonr": 0.5462466301359132
    },
    "tdcommons/lipophilicity-astrazeneca": {
        "mean_absolute_error": 0.7925310842451595
    },
    "tdcommons/ppbr-az": {
        "mean_absolute_error": 8.370688843428555
    },
    "tdcommons/clearance-hepatocyte-az": {
        "spearmanr": 0.3720101407055169
    },
    "tdcommons/cyp2d6-substrate-carbonmangels": {
        "pr_auc": 0.6257065412155716
    },
    "tdcommons/half-life-obach": {
        "spearmanr": 0.499095111850241
    },
    "tdcommons/cyp2c9-substrate-carbonmangels": {
        "pr_auc": 0.4166753939077579
    },
    "tdcommons/clearance-microsome-az": {
        "spearmanr": 0.558387249929121
    },
    "tdcommons/dili": {
        "roc_auc": 0.9369565217391305
    },
    "tdcommons/bioavailability-ma": {
        "roc_auc": 0.6431659461257067
    },
    "tdcommons/vdss-lombardo": {
        "spearmanr": 0.5890949017713104
    },
    "tdcommons/cyp3a4-substrate-carbonmangels": {
        "roc_auc": 0.6421790235081375
    },
    "tdcommons/pgp-broccatelli": {
        "roc_auc": 0.9048253798986936
    },
    "tdcommons/caco2-wang": {
        "mean_absolute_error": 0.3120707883049934
    },
    "tdcommons/herg": {
        "roc_auc": 0.8131075110456554
    },
    "tdcommons/bbb-martins": {
        "roc_auc": 0.8494957786116323
    },
    "tdcommons/ames": {
        "roc_auc": 0.763221328007206
    },
    "tdcommons/ld50-zhu": {
        "mean_absolute_error": 0.683485942748306
    }
}

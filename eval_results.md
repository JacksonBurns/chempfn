# Eval Results

timestamp: 2026-07-14 11:14:10.453499
reg_checkpoint: reg.ckpt
cls_checkpoint: cls.ckpt

## `polaris/pkis2-ret-wt-cls-v2`

### Model Performance
|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | pr_auc      | 0.673439 |
|  1 | test       | CLS_RET        | cohen_kappa | 0.509638 |
|  2 | test       | CLS_RET        | accuracy    | 0.886792 |
|  3 | test       | CLS_RET        | mcc         | 0.525683 |
|  4 | test       | CLS_RET        | roc_auc     | 0.818242 |
|  5 | test       | CLS_RET        | f1          | 0.571429 |

### Leaderboard Comparison
| Name                                 |   pr_auc |
|:-------------------------------------|---------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics   | 0.885    |
| 1B_MolGPS-ens_LargeMix-and-Phenomics | 0.879    |
| ChemPFN                              | 0.673439 |
| CheMeleon                            | 0.639    |
| MHNfs                                | 0.417    |

## `polaris/pkis2-ret-wt-reg-v2`

### Model Performance
|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | RET            | spearmanr           |   0.594534 |
|  1 | test       | RET            | mean_squared_error  | 798.444    |
|  2 | test       | RET            | mean_absolute_error |  22.0459   |
|  3 | test       | RET            | r2                  |   0.327572 |
|  4 | test       | RET            | pearsonr            |   0.638416 |
|  5 | test       | RET            | explained_var       |   0.34434  |

### Leaderboard Comparison
| Name                                 |   mean_squared_error |
|:-------------------------------------|---------------------:|
| 1B_MolGPS-ens_LargeMix-and-Phenomics |              589.944 |
| 3B_e50_MPNN_LargeMix-and-Phenomics   |              609.399 |
| CheMeleon                            |              684.319 |
| CheMeleon                            |              724.347 |
| ChemPFN                              |              798.444 |

## `polaris/pkis2-kit-wt-cls-v2`

### Model Performance
|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | pr_auc      | 0.600489 |
|  1 | test       | CLS_KIT        | cohen_kappa | 0.458404 |
|  2 | test       | CLS_KIT        | accuracy    | 0.810345 |
|  3 | test       | CLS_KIT        | mcc         | 0.467561 |
|  4 | test       | CLS_KIT        | roc_auc     | 0.797872 |
|  5 | test       | CLS_KIT        | f1          | 0.576923 |

### Leaderboard Comparison
| Name      |   pr_auc |
|:----------|---------:|
| CheMeleon | 0.646    |
| ChemPFN   | 0.600489 |
| MHNfs     | 0.376    |

## `polaris/pkis2-kit-wt-reg-v2`

### Model Performance
|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | KIT            | spearmanr           |   0.488237 |
|  1 | test       | KIT            | mean_squared_error  | 870.991    |
|  2 | test       | KIT            | mean_absolute_error |  22.7731   |
|  3 | test       | KIT            | r2                  |   0.278194 |
|  4 | test       | KIT            | pearsonr            |   0.576024 |
|  5 | test       | KIT            | explained_var       |   0.330431 |

### Leaderboard Comparison
| Name      |   mean_squared_error |
|:----------|---------------------:|
| CheMeleon |              849.611 |
| ChemPFN   |              870.991 |

## `polaris/pkis2-egfr-wt-reg-v2`

### Model Performance
|    | Test set   | Target label   | Metric              |      Score |
|---:|:-----------|:---------------|:--------------------|-----------:|
|  0 | test       | EGFR           | spearmanr           |   0.371167 |
|  1 | test       | EGFR           | mean_squared_error  | 442.136    |
|  2 | test       | EGFR           | mean_absolute_error |  17.1133   |
|  3 | test       | EGFR           | r2                  |   0.451287 |
|  4 | test       | EGFR           | pearsonr            |   0.688312 |
|  5 | test       | EGFR           | explained_var       |   0.460429 |

### Leaderboard Comparison
| Name                                   |   mean_squared_error |
|:---------------------------------------|---------------------:|
| aether-pharmaos-pkis2-egfr-wt-ensemble |              430.821 |
| ChemPFN                                |              442.136 |
| CheMeleon                              |              459.929 |

## `polaris/adme-fang-solu-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_SOLUBILITY | spearmanr           | 0.525433 |
|  1 | test       | LOG_SOLUBILITY | mean_squared_error  | 0.344936 |
|  2 | test       | LOG_SOLUBILITY | mean_absolute_error | 0.420086 |
|  3 | test       | LOG_SOLUBILITY | r2                  | 0.363796 |
|  4 | test       | LOG_SOLUBILITY | pearsonr            | 0.612761 |
|  5 | test       | LOG_SOLUBILITY | explained_var       | 0.365679 |

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
| ChemPFN                     |   0.612761 |

## `polaris/adme-fang-rppb-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RPPB       | spearmanr           | 0.886957 |
|  1 | test       | LOG_RPPB       | mean_squared_error  | 0.36385  |
|  2 | test       | LOG_RPPB       | mean_absolute_error | 0.463114 |
|  3 | test       | LOG_RPPB       | r2                  | 0.590481 |
|  4 | test       | LOG_RPPB       | pearsonr            | 0.821978 |
|  5 | test       | LOG_RPPB       | explained_var       | 0.609843 |

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
|  0 | test       | LOG_HPPB       | spearmanr           | 0.811674 |
|  1 | test       | LOG_HPPB       | mean_squared_error  | 0.250799 |
|  2 | test       | LOG_HPPB       | mean_absolute_error | 0.428223 |
|  3 | test       | LOG_HPPB       | r2                  | 0.585894 |
|  4 | test       | LOG_HPPB       | pearsonr            | 0.80736  |
|  5 | test       | LOG_HPPB       | explained_var       | 0.636756 |

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
|  0 | test       | LOG_MDR1-MDCK_ER | spearmanr           | 0.720765 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  | 0.23817  |
|  2 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error | 0.383879 |
|  3 | test       | LOG_MDR1-MDCK_ER | r2                  | 0.51923  |
|  4 | test       | LOG_MDR1-MDCK_ER | pearsonr            | 0.736755 |
|  5 | test       | LOG_MDR1-MDCK_ER | explained_var       | 0.522487 |

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
| ChemPFN                                       |   0.736755 |
| optimized-random-forest-rdkit-descriptors     |   0.727    |
| adme-fang-PERM-1_desc2D_RandomForestRegressor |   0.716    |
| chemlactica-125m-sft                          |   0.714    |

## `polaris/adme-fang-rclint-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_RLM_CLint  | spearmanr           | 0.622225 |
|  1 | test       | LOG_RLM_CLint  | mean_squared_error  | 0.344852 |
|  2 | test       | LOG_RLM_CLint  | mean_absolute_error | 0.475988 |
|  3 | test       | LOG_RLM_CLint  | r2                  | 0.389149 |
|  4 | test       | LOG_RLM_CLint  | pearsonr            | 0.626507 |
|  5 | test       | LOG_RLM_CLint  | explained_var       | 0.390925 |

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
| ChemPFN                                         |   0.626507 |
| adme-fang-RCLint-1_desc2D_FCModel               |   0.544    |

## `polaris/adme-fang-hclint-1`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | LOG_HLM_CLint  | spearmanr           | 0.607588 |
|  1 | test       | LOG_HLM_CLint  | mean_squared_error  | 0.245813 |
|  2 | test       | LOG_HLM_CLint  | mean_absolute_error | 0.41713  |
|  3 | test       | LOG_HLM_CLint  | r2                  | 0.36713  |
|  4 | test       | LOG_HLM_CLint  | pearsonr            | 0.610793 |
|  5 | test       | LOG_HLM_CLint  | explained_var       | 0.368745 |

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
| ChemPFN                                         |   0.610793 |

## `tdcommons/lipophilicity-astrazeneca`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.729392 |

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
| ChemPFN                                   |              0.729392 |

## `tdcommons/ppbr-az`

### Model Performance
|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error |  9.9945 |

### Leaderboard Comparison
| Name                               |   mean_absolute_error |
|:-----------------------------------|----------------------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics |                7.004  |
| 1B_MPNN_LargeMix-and-Phenomics     |                7.026  |
| TabPFNv2-rdkit-3D                  |                7.033  |
| TabPFNv2-rdkit                     |                7.117  |
| CheMeleon                          |                7.532  |
| ChemPFN                            |                9.9945 |

## `tdcommons/clearance-hepatocyte-az`

### Model Performance
|    | Test set   | Target label   | Metric    |   Score |
|---:|:-----------|:---------------|:----------|--------:|
|  0 | test       | Y              | spearmanr | 0.37088 |

### Leaderboard Comparison
| Name                                |   spearmanr |
|:------------------------------------|------------:|
| 1B_MPNN_LargeMix-and-Phenomics      |     0.538   |
| 3B_e50_MPNN_LargeMix-and-Phenomics  |     0.525   |
| clearance-hepatocyte-az-GIRAFFE-wae |     0.429   |
| TabPFNv2-rdkit                      |     0.41    |
| TabPFNv2-rdkit-3D                   |     0.402   |
| CheMeleon                           |     0.387   |
| ChemPFN                             |     0.37088 |

## `tdcommons/cyp2d6-substrate-carbonmangels`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.629274 |

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
| ChemPFN                                      | 0.629274 |
| ARKA-Mordred                                 | 0.558    |

## `tdcommons/half-life-obach`

### Model Performance
|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.458758 |

### Leaderboard Comparison
| Name                               |   spearmanr |
|:-----------------------------------|------------:|
| 1B_MPNN_LargeMix-and-Phenomics     |    0.625    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |    0.573    |
| TabPFNv2-rdkit                     |    0.542    |
| TabPFNv2-rdkit-3D                  |    0.489    |
| ChemPFN                            |    0.458758 |
| MolEncoder                         |    0.417    |
| CheMeleon                          |    0.36     |

## `tdcommons/cyp2c9-substrate-carbonmangels`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.452645 |

### Leaderboard Comparison
| Name                               |   pr_auc |
|:-----------------------------------|---------:|
| 1B_MPNN_LargeMix-and-Phenomics     | 0.478    |
| CheMeleon                          | 0.47     |
| ChemPFN                            | 0.452645 |
| 3B_e50_MPNN_LargeMix-and-Phenomics | 0.407    |
| TabPFNv2-rdkit                     | 0.378    |
| MHNfs                              | 0.276    |

## `tdcommons/clearance-microsome-az`

### Model Performance
|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.561632 |

### Leaderboard Comparison
| Name                               |   spearmanr |
|:-----------------------------------|------------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics |    0.683    |
| 1B_MPNN_LargeMix-and-Phenomics     |    0.653    |
| TabPFNv2-rdkit-3D                  |    0.649    |
| TabPFNv2-rdkit                     |    0.64     |
| CheMeleon                          |    0.59     |
| ChemPFN                            |    0.561632 |

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
|  0 | test       | Y              | roc_auc  | 0.698703 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| vidraft-tabpfn-ensemble-bioavail   |  0.734    |
| TabPFNv2-rdkit-3D                  |  0.729    |
| TabPFNv2-rdkit                     |  0.728    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.714    |
| ChemPFN                            |  0.698703 |
| CheMeleon                          |  0.698    |
| 1B_MPNN_LargeMix-and-Phenomics     |  0.675    |
| MHNfs                              |  0.61     |

## `tdcommons/vdss-lombardo`

### Model Performance
|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.520453 |

### Leaderboard Comparison
| Name                               |   spearmanr |
|:-----------------------------------|------------:|
| vidraft-tabpfn-vdss                |    0.726    |
| TabPFNv2-rdkit                     |    0.7      |
| TabPFNv2-rdkit-3D                  |    0.69     |
| 1B_MPNN_LargeMix-and-Phenomics     |    0.637    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |    0.6      |
| CheMeleon                          |    0.59     |
| ChemPFN                            |    0.520453 |

## `tdcommons/cyp3a4-substrate-carbonmangels`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.643535 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| 1B_MPNN_LargeMix-and-Phenomics     |  0.696    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.685    |
| ChemPFN                            |  0.643535 |
| TabPFNv2-rdkit                     |  0.634    |
| TabPFNv2-rdkit-3D                  |  0.622    |
| CheMeleon                          |  0.606    |

## `tdcommons/pgp-broccatelli`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.883898 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| 1B_MPNN_LargeMix-and-Phenomics     |  0.954    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.942    |
| TabPFNv2-rdkit                     |  0.941    |
| TabPFNv2-rdkit-3D                  |  0.93     |
| CheMeleon                          |  0.911    |
| ChemPFN                            |  0.883898 |
| MHNfs                              |  0.834    |

## `tdcommons/caco2-wang`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.322873 |

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
| ChemPFN                                   |              0.322873 |

## `tdcommons/herg`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.818262 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| agentomics-ml-herg                 |  0.892    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.891    |
| 1B_MPNN_LargeMix-and-Phenomics     |  0.855    |
| TabPFNv2-rdkit                     |  0.849    |
| TabPFNv2-rdkit-3D                  |  0.848    |
| CheMeleon                          |  0.822    |
| ChemPFN                            |  0.818262 |
| 1B_MPNN_LargeMix                   |  0.816    |
| MHNfs                              |  0.671    |

## `tdcommons/bbb-martins`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.850121 |

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
| ChemPFN                            |  0.850121 |
| MHNfs                              |  0.616    |

## `tdcommons/ames`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.785702 |

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
| ChemPFN                            |  0.785702 |

## `tdcommons/ld50-zhu`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.611555 |

### Leaderboard Comparison
| Name                               |   mean_absolute_error |
|:-----------------------------------|----------------------:|
| CheMeleon                          |              0.526    |
| TabPFNv2-rdkit                     |              0.6      |
| TabPFNv2-rdkit-3D                  |              0.605    |
| ChemPFN                            |              0.611555 |
| 1B_MPNN_LargeMix-and-Phenomics     |              0.614    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |              0.625    |

# Summary

Average Rank of ChemPFN across benchmarks with 4+ other entries 25: 6.72

results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": {
        "pr_auc": 0.6734386468178029
    },
    "polaris/pkis2-ret-wt-reg-v2": {
        "mean_squared_error": 798.4444227534887
    },
    "polaris/pkis2-kit-wt-cls-v2": {
        "pr_auc": 0.6004890019538361
    },
    "polaris/pkis2-kit-wt-reg-v2": {
        "mean_squared_error": 870.9913408473478
    },
    "polaris/pkis2-egfr-wt-reg-v2": {
        "mean_squared_error": 442.13563883311963
    },
    "polaris/adme-fang-solu-1": {
        "pearsonr": 0.6127608750074969
    },
    "polaris/adme-fang-rppb-1": {
        "pearsonr": 0.8219779431694072
    },
    "polaris/adme-fang-hppb-1": {
        "pearsonr": 0.8073597664740543
    },
    "polaris/adme-fang-perm-1": {
        "pearsonr": 0.7367546289045529
    },
    "polaris/adme-fang-rclint-1": {
        "pearsonr": 0.6265066813194985
    },
    "polaris/adme-fang-hclint-1": {
        "pearsonr": 0.6107934249001227
    },
    "tdcommons/lipophilicity-astrazeneca": {
        "mean_absolute_error": 0.7293924177941822
    },
    "tdcommons/ppbr-az": {
        "mean_absolute_error": 9.994498616936808
    },
    "tdcommons/clearance-hepatocyte-az": {
        "spearmanr": 0.3708799289207338
    },
    "tdcommons/cyp2d6-substrate-carbonmangels": {
        "pr_auc": 0.629274215906942
    },
    "tdcommons/half-life-obach": {
        "spearmanr": 0.4587579359303712
    },
    "tdcommons/cyp2c9-substrate-carbonmangels": {
        "pr_auc": 0.45264467412097187
    },
    "tdcommons/clearance-microsome-az": {
        "spearmanr": 0.5616322869746391
    },
    "tdcommons/dili": {
        "roc_auc": 0.9360869565217391
    },
    "tdcommons/bioavailability-ma": {
        "roc_auc": 0.6987030262720318
    },
    "tdcommons/vdss-lombardo": {
        "spearmanr": 0.5204528265597166
    },
    "tdcommons/cyp3a4-substrate-carbonmangels": {
        "roc_auc": 0.6435352622061483
    },
    "tdcommons/pgp-broccatelli": {
        "roc_auc": 0.8838976272993868
    },
    "tdcommons/caco2-wang": {
        "mean_absolute_error": 0.32287254136617477
    },
    "tdcommons/herg": {
        "roc_auc": 0.8182621502209131
    },
    "tdcommons/bbb-martins": {
        "roc_auc": 0.8501211694809256
    },
    "tdcommons/ames": {
        "roc_auc": 0.7857016977031075
    },
    "tdcommons/ld50-zhu": {
        "mean_absolute_error": 0.6115550384953798
    }
}

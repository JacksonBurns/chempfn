# Eval Results

timestamp: 2026-07-14 11:06:48.713289
reg_checkpoint: cls.ckpt
cls_checkpoint: reg.ckpt

## `polaris/pkis2-ret-wt-cls-v2`

### Model Performance
|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_RET        | accuracy    | 0.886792 |
|  1 | test       | CLS_RET        | f1          | 0.571429 |
|  2 | test       | CLS_RET        | cohen_kappa | 0.509638 |
|  3 | test       | CLS_RET        | roc_auc     | 0.839392 |
|  4 | test       | CLS_RET        | mcc         | 0.525683 |
|  5 | test       | CLS_RET        | pr_auc      | 0.65303  |

### Leaderboard Comparison
| Name                                 |   pr_auc |
|:-------------------------------------|---------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics   |  0.885   |
| 1B_MolGPS-ens_LargeMix-and-Phenomics |  0.879   |
| ChemPFN                              |  0.65303 |
| CheMeleon                            |  0.639   |
| MHNfs                                |  0.417   |

## `polaris/pkis2-ret-wt-reg-v2`

### Model Performance
|    | Test set   | Target label   | Metric              |          Score |
|---:|:-----------|:---------------|:--------------------|---------------:|
|  0 | test       | RET            | explained_var       |    2.10928e-05 |
|  1 | test       | RET            | mean_absolute_error |   36.0043      |
|  2 | test       | RET            | spearmanr           |    0.0177085   |
|  3 | test       | RET            | mean_squared_error  | 1498.35        |
|  4 | test       | RET            | r2                  |   -0.26187     |
|  5 | test       | RET            | pearsonr            |    0.00464951  |

### Leaderboard Comparison
| Name                                 |   mean_squared_error |
|:-------------------------------------|---------------------:|
| 1B_MolGPS-ens_LargeMix-and-Phenomics |              589.944 |
| 3B_e50_MPNN_LargeMix-and-Phenomics   |              609.399 |
| CheMeleon                            |              684.319 |
| CheMeleon                            |              724.347 |
| ChemPFN                              |             1498.35  |

## `polaris/pkis2-kit-wt-cls-v2`

### Model Performance
|    | Test set   | Target label   | Metric      |    Score |
|---:|:-----------|:---------------|:------------|---------:|
|  0 | test       | CLS_KIT        | accuracy    | 0.75     |
|  1 | test       | CLS_KIT        | f1          | 0.491228 |
|  2 | test       | CLS_KIT        | cohen_kappa | 0.336751 |
|  3 | test       | CLS_KIT        | roc_auc     | 0.733559 |
|  4 | test       | CLS_KIT        | mcc         | 0.3527   |
|  5 | test       | CLS_KIT        | pr_auc      | 0.549174 |

### Leaderboard Comparison
| Name      |   pr_auc |
|:----------|---------:|
| CheMeleon | 0.646    |
| ChemPFN   | 0.549174 |
| MHNfs     | 0.376    |

## `polaris/pkis2-kit-wt-reg-v2`

### Model Performance
|    | Test set   | Target label   | Metric              |          Score |
|---:|:-----------|:---------------|:--------------------|---------------:|
|  0 | test       | KIT            | explained_var       |   -0.000610161 |
|  1 | test       | KIT            | mean_absolute_error |   32.9509      |
|  2 | test       | KIT            | spearmanr           |   -0.116256    |
|  3 | test       | KIT            | mean_squared_error  | 1304.33        |
|  4 | test       | KIT            | r2                  |   -0.0809193   |
|  5 | test       | KIT            | pearsonr            |   -0.072222    |

### Leaderboard Comparison
| Name      |   mean_squared_error |
|:----------|---------------------:|
| CheMeleon |              849.611 |
| ChemPFN   |             1304.33  |

## `polaris/pkis2-egfr-wt-reg-v2`

### Model Performance
|    | Test set   | Target label   | Metric              |          Score |
|---:|:-----------|:---------------|:--------------------|---------------:|
|  0 | test       | EGFR           | explained_var       |    0.000728672 |
|  1 | test       | EGFR           | mean_absolute_error |   33.3162      |
|  2 | test       | EGFR           | spearmanr           |   -0.0274923   |
|  3 | test       | EGFR           | mean_squared_error  | 1315.86        |
|  4 | test       | EGFR           | r2                  |   -0.633055    |
|  5 | test       | EGFR           | pearsonr            |    0.0709032   |

### Leaderboard Comparison
| Name                                   |   mean_squared_error |
|:---------------------------------------|---------------------:|
| aether-pharmaos-pkis2-egfr-wt-ensemble |              430.821 |
| CheMeleon                              |              459.929 |
| ChemPFN                                |             1315.86  |

## `polaris/adme-fang-solu-1`

### Model Performance
|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | LOG_SOLUBILITY | explained_var       |  0.000966304 |
|  1 | test       | LOG_SOLUBILITY | mean_absolute_error |  0.927882    |
|  2 | test       | LOG_SOLUBILITY | spearmanr           |  0.013415    |
|  3 | test       | LOG_SOLUBILITY | mean_squared_error  |  0.947495    |
|  4 | test       | LOG_SOLUBILITY | r2                  | -0.74757     |
|  5 | test       | LOG_SOLUBILITY | pearsonr            |  0.0523313   |

### Leaderboard Comparison
| Name                        |   pearsonr |
|:----------------------------|-----------:|
| 1B_MPNN_MolGPS-ens_LargeMix |  0.77      |
| 1B_MPNN_LargeMix-Phenomics  |  0.764     |
| CheMeleonMOE                |  0.729     |
| CheMeleon                   |  0.682     |
| it-works-now                |  0.669     |
| ML4DD-team16                |  0.654     |
| ML4DD-team9                 |  0.651     |
| team9_submission_2          |  0.651     |
| ExactTanimotoGP             |  0.635     |
| ML4DD-team25                |  0.632     |
| ChemPFN                     |  0.0523313 |

## `polaris/adme-fang-rppb-1`

### Model Performance
|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | LOG_RPPB       | explained_var       | -0.00124621 |
|  1 | test       | LOG_RPPB       | mean_absolute_error |  0.970924   |
|  2 | test       | LOG_RPPB       | spearmanr           | -0.0547826  |
|  3 | test       | LOG_RPPB       | mean_squared_error  |  1.20939    |
|  4 | test       | LOG_RPPB       | r2                  | -0.361183   |
|  5 | test       | LOG_RPPB       | pearsonr            | -0.100069   |

### Leaderboard Comparison
| Name                                          |   pearsonr |
|:----------------------------------------------|-----------:|
| 1B_MPNN_LargeMix-and-Phenomics                |   0.908    |
| 1B_MPNN_MolGPS-ens_LargeMix                   |   0.886    |
| nepare                                        |   0.863    |
| TabPFNv2-rdkit                                |   0.816    |
| nepare_chemprop                               |   0.78     |
| chemma-2b-sft                                 |   0.747    |
| adme-fang-RPPB-1_desc2D_RandomForestRegressor |   0.722    |
| adme-fang-RPPB-1-GIRAFFE-wae                  |   0.68     |
| CheMeleon                                     |   0.662    |
| chemlactica-1b-sft                            |   0.614    |
| ChemPFN                                       |  -0.100069 |

## `polaris/adme-fang-hppb-1`

### Model Performance
|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | LOG_HPPB       | explained_var       | -0.00473884 |
|  1 | test       | LOG_HPPB       | mean_absolute_error |  0.877259   |
|  2 | test       | LOG_HPPB       | spearmanr           | -0.234548   |
|  3 | test       | LOG_HPPB       | mean_squared_error  |  1.04413    |
|  4 | test       | LOG_HPPB       | r2                  | -0.724021   |
|  5 | test       | LOG_HPPB       | pearsonr            | -0.205864   |

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
| adme-fang-HPPB-1_atompair_RandomForestRegressor |   0.69     |
| chemma-2b-sft                                   |   0.636    |
| ChemPFN                                         |  -0.205864 |

## `polaris/adme-fang-perm-1`

### Model Performance
|    | Test set   | Target label     | Metric              |       Score |
|---:|:-----------|:-----------------|:--------------------|------------:|
|  0 | test       | LOG_MDR1-MDCK_ER | explained_var       |  0.00190485 |
|  1 | test       | LOG_MDR1-MDCK_ER | mean_absolute_error |  0.672472   |
|  2 | test       | LOG_MDR1-MDCK_ER | spearmanr           |  0.0982126  |
|  3 | test       | LOG_MDR1-MDCK_ER | mean_squared_error  |  0.560477   |
|  4 | test       | LOG_MDR1-MDCK_ER | r2                  | -0.131379   |
|  5 | test       | LOG_MDR1-MDCK_ER | pearsonr            |  0.0931817  |

### Leaderboard Comparison
| Name                                          |   pearsonr |
|:----------------------------------------------|-----------:|
| 1B_MPNN_MolGPS-ens_LargeMix                   |  0.879     |
| 1B_MPNN_LargeMix-and-Phenomics                |  0.86      |
| CheMeleon                                     |  0.822     |
| MolEncoder                                    |  0.804     |
| TabPFNv2-rdkit                                |  0.798     |
| adme-fang-PERM-1-GIRAFFE-wae_s                |  0.772     |
| chemlactica-1b-sft                            |  0.762     |
| optimized-random-forest-rdkit-descriptors     |  0.727     |
| adme-fang-PERM-1_desc2D_RandomForestRegressor |  0.716     |
| chemlactica-125m-sft                          |  0.714     |
| ChemPFN                                       |  0.0931817 |

## `polaris/adme-fang-rclint-1`

### Model Performance
|    | Test set   | Target label   | Metric              |        Score |
|---:|:-----------|:---------------|:--------------------|-------------:|
|  0 | test       | LOG_RLM_CLint  | explained_var       |  0.000547229 |
|  1 | test       | LOG_RLM_CLint  | mean_absolute_error |  0.649722    |
|  2 | test       | LOG_RLM_CLint  | spearmanr           |  0.0297664   |
|  3 | test       | LOG_RLM_CLint  | mean_squared_error  |  0.61783     |
|  4 | test       | LOG_RLM_CLint  | r2                  | -0.0943892   |
|  5 | test       | LOG_RLM_CLint  | pearsonr            |  0.0348701   |

### Leaderboard Comparison
| Name                                            |   pearsonr |
|:------------------------------------------------|-----------:|
| 1B_MPNN_MolGPS-ens_LargeMix                     |  0.798     |
| 1B_MPNN_LargeMix-and-Phenomics                  |  0.784     |
| CheMeleon                                       |  0.757     |
| chemlactica-125m-sft                            |  0.714     |
| chemlactica-1b-sft                              |  0.698     |
| TabPFNv2-rdkit                                  |  0.694     |
| chemma-2b-sft                                   |  0.66      |
| adme-fang-RCLint-1_desc2D_RandomForestRegressor |  0.64      |
| adme-fang-RCLint-1_desc2D_RandomForestRegressor |  0.631     |
| adme-fang-RCLint-1_desc2D_FCModel               |  0.544     |
| ChemPFN                                         |  0.0348701 |

## `polaris/adme-fang-hclint-1`

### Model Performance
|    | Test set   | Target label   | Metric              |       Score |
|---:|:-----------|:---------------|:--------------------|------------:|
|  0 | test       | LOG_HLM_CLint  | explained_var       |  0.00112978 |
|  1 | test       | LOG_HLM_CLint  | mean_absolute_error |  0.768712   |
|  2 | test       | LOG_HLM_CLint  | spearmanr           |  0.0879217  |
|  3 | test       | LOG_HLM_CLint  | mean_squared_error  |  0.80032    |
|  4 | test       | LOG_HLM_CLint  | r2                  | -1.0605     |
|  5 | test       | LOG_HLM_CLint  | pearsonr            |  0.0672958  |

### Leaderboard Comparison
| Name                                            |   pearsonr |
|:------------------------------------------------|-----------:|
| seqera-gradient                                 |  0.796     |
| 1B_MPNN_LargeMix-and-Phenomics                  |  0.778     |
| chemlactica-1b-sft                              |  0.72      |
| CheMeleon                                       |  0.72      |
| chemlactica-125m-sft                            |  0.717     |
| MolEncoder                                      |  0.714     |
| agentomics-ml-adme-fang-hclint-1                |  0.697     |
| chemma-2b-sft                                   |  0.674     |
| TabPFNv2-rdkit                                  |  0.662     |
| adme-fang-HCLint-1_desc2D_RandomForestRegressor |  0.639     |
| ChemPFN                                         |  0.0672958 |

## `tdcommons/lipophilicity-astrazeneca`

### Model Performance
|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 1.23396 |

### Leaderboard Comparison
| Name                                      |   mean_absolute_error |
|:------------------------------------------|----------------------:|
| 1B_MPNN_MolGPS-ens_LargeMix-and-Phenomics |               0.392   |
| 1B_MPNN_LargeMix-and-Phenomics            |               0.411   |
| 3B_e50_MPNN_LargeMix-and-Phenomics        |               0.424   |
| CheMeleon                                 |               0.443   |
| MolEncoder                                |               0.497   |
| agentomics-ml-lipophilicity-astrazeneca   |               0.497   |
| TabPFNv2-rdkit                            |               0.499   |
| TabPFNv2-rdkit                            |               0.502   |
| TabPFNv2-maplight_gnn                     |               0.502   |
| TabPFNv2-rdkit-3D                         |               0.524   |
| ChemPFN                                   |               1.23396 |

## `tdcommons/ppbr-az`

### Model Performance
|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 34.4591 |

### Leaderboard Comparison
| Name                               |   mean_absolute_error |
|:-----------------------------------|----------------------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics |                7.004  |
| 1B_MPNN_LargeMix-and-Phenomics     |                7.026  |
| TabPFNv2-rdkit-3D                  |                7.033  |
| TabPFNv2-rdkit                     |                7.117  |
| CheMeleon                          |                7.532  |
| ChemPFN                            |               34.4591 |

## `tdcommons/clearance-hepatocyte-az`

### Model Performance
|    | Test set   | Target label   | Metric    |      Score |
|---:|:-----------|:---------------|:----------|-----------:|
|  0 | test       | Y              | spearmanr | -0.0590503 |

### Leaderboard Comparison
| Name                                |   spearmanr |
|:------------------------------------|------------:|
| 1B_MPNN_LargeMix-and-Phenomics      |   0.538     |
| 3B_e50_MPNN_LargeMix-and-Phenomics  |   0.525     |
| clearance-hepatocyte-az-GIRAFFE-wae |   0.429     |
| TabPFNv2-rdkit                      |   0.41      |
| TabPFNv2-rdkit-3D                   |   0.402     |
| CheMeleon                           |   0.387     |
| ChemPFN                             |  -0.0590503 |

## `tdcommons/cyp2d6-substrate-carbonmangels`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.494113 |

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
| ARKA-Mordred                                 | 0.558    |
| ChemPFN                                      | 0.494113 |

## `tdcommons/half-life-obach`

### Model Performance
|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.107691 |

### Leaderboard Comparison
| Name                               |   spearmanr |
|:-----------------------------------|------------:|
| 1B_MPNN_LargeMix-and-Phenomics     |    0.625    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |    0.573    |
| TabPFNv2-rdkit                     |    0.542    |
| TabPFNv2-rdkit-3D                  |    0.489    |
| MolEncoder                         |    0.417    |
| CheMeleon                          |    0.36     |
| ChemPFN                            |    0.107691 |

## `tdcommons/cyp2c9-substrate-carbonmangels`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | pr_auc   | 0.356216 |

### Leaderboard Comparison
| Name                               |   pr_auc |
|:-----------------------------------|---------:|
| 1B_MPNN_LargeMix-and-Phenomics     | 0.478    |
| CheMeleon                          | 0.47     |
| 3B_e50_MPNN_LargeMix-and-Phenomics | 0.407    |
| TabPFNv2-rdkit                     | 0.378    |
| ChemPFN                            | 0.356216 |
| MHNfs                              | 0.276    |

## `tdcommons/clearance-microsome-az`

### Model Performance
|    | Test set   | Target label   | Metric    |    Score |
|---:|:-----------|:---------------|:----------|---------:|
|  0 | test       | Y              | spearmanr | 0.248828 |

### Leaderboard Comparison
| Name                               |   spearmanr |
|:-----------------------------------|------------:|
| 3B_e50_MPNN_LargeMix-and-Phenomics |    0.683    |
| 1B_MPNN_LargeMix-and-Phenomics     |    0.653    |
| TabPFNv2-rdkit-3D                  |    0.649    |
| TabPFNv2-rdkit                     |    0.64     |
| CheMeleon                          |    0.59     |
| ChemPFN                            |    0.248828 |

## `tdcommons/dili`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.868696 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| vidraft-structure-ensemble-dili    |  0.933    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.933    |
| TabPFNv2-rdkit-3D                  |  0.93     |
| 1B_MPNN_LargeMix-and-Phenomics     |  0.925    |
| CheMeleon                          |  0.916    |
| TabPFNv2-rdkit                     |  0.9      |
| ChemPFN                            |  0.868696 |

## `tdcommons/bioavailability-ma`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.627536 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| vidraft-tabpfn-ensemble-bioavail   |  0.734    |
| TabPFNv2-rdkit-3D                  |  0.729    |
| TabPFNv2-rdkit                     |  0.728    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.714    |
| CheMeleon                          |  0.698    |
| 1B_MPNN_LargeMix-and-Phenomics     |  0.675    |
| ChemPFN                            |  0.627536 |
| MHNfs                              |  0.61     |

## `tdcommons/vdss-lombardo`

### Model Performance
|    | Test set   | Target label   | Metric    |     Score |
|---:|:-----------|:---------------|:----------|----------:|
|  0 | test       | Y              | spearmanr | 0.0641546 |

### Leaderboard Comparison
| Name                               |   spearmanr |
|:-----------------------------------|------------:|
| vidraft-tabpfn-vdss                |   0.726     |
| TabPFNv2-rdkit                     |   0.7       |
| TabPFNv2-rdkit-3D                  |   0.69      |
| 1B_MPNN_LargeMix-and-Phenomics     |   0.637     |
| 3B_e50_MPNN_LargeMix-and-Phenomics |   0.6       |
| CheMeleon                          |   0.59      |
| ChemPFN                            |   0.0641546 |

## `tdcommons/cyp3a4-substrate-carbonmangels`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.593128 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| 1B_MPNN_LargeMix-and-Phenomics     |  0.696    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.685    |
| TabPFNv2-rdkit                     |  0.634    |
| TabPFNv2-rdkit-3D                  |  0.622    |
| CheMeleon                          |  0.606    |
| ChemPFN                            |  0.593128 |

## `tdcommons/pgp-broccatelli`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.824447 |

### Leaderboard Comparison
| Name                               |   roc_auc |
|:-----------------------------------|----------:|
| 1B_MPNN_LargeMix-and-Phenomics     |  0.954    |
| 3B_e50_MPNN_LargeMix-and-Phenomics |  0.942    |
| TabPFNv2-rdkit                     |  0.941    |
| TabPFNv2-rdkit-3D                  |  0.93     |
| CheMeleon                          |  0.911    |
| MHNfs                              |  0.834    |
| ChemPFN                            |  0.824447 |

## `tdcommons/caco2-wang`

### Model Performance
|    | Test set   | Target label   | Metric              |    Score |
|---:|:-----------|:---------------|:--------------------|---------:|
|  0 | test       | Y              | mean_absolute_error | 0.615986 |

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
| ChemPFN                                   |              0.615986 |

## `tdcommons/herg`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.699705 |

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
| ChemPFN                            |  0.699705 |
| MHNfs                              |  0.671    |

## `tdcommons/bbb-martins`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.813829 |

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
| ChemPFN                            |  0.813829 |
| MHNfs                              |  0.616    |

## `tdcommons/ames`

### Model Performance
|    | Test set   | Target label   | Metric   |    Score |
|---:|:-----------|:---------------|:---------|---------:|
|  0 | test       | Y              | roc_auc  | 0.701633 |

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
| ChemPFN                            |  0.701633 |

## `tdcommons/ld50-zhu`

### Model Performance
|    | Test set   | Target label   | Metric              |   Score |
|---:|:-----------|:---------------|:--------------------|--------:|
|  0 | test       | Y              | mean_absolute_error | 1.04739 |

### Leaderboard Comparison
| Name                               |   mean_absolute_error |
|:-----------------------------------|----------------------:|
| CheMeleon                          |               0.526   |
| TabPFNv2-rdkit                     |               0.6     |
| TabPFNv2-rdkit-3D                  |               0.605   |
| 1B_MPNN_LargeMix-and-Phenomics     |               0.614   |
| 3B_e50_MPNN_LargeMix-and-Phenomics |               0.625   |
| ChemPFN                            |               1.04739 |

# Summary

Average Rank of ChemPFN across benchmarks with 4+ other entries 25: 8.12

results_dict = {
    "polaris/pkis2-ret-wt-cls-v2": {
        "pr_auc": 0.6530303748943341
    },
    "polaris/pkis2-ret-wt-reg-v2": {
        "mean_squared_error": 1498.3511812005358
    },
    "polaris/pkis2-kit-wt-cls-v2": {
        "pr_auc": 0.5491742935088788
    },
    "polaris/pkis2-kit-wt-reg-v2": {
        "mean_squared_error": 1304.328120973853
    },
    "polaris/pkis2-egfr-wt-reg-v2": {
        "mean_squared_error": 1315.8644027696698
    },
    "polaris/adme-fang-solu-1": {
        "pearsonr": 0.05233126545137837
    },
    "polaris/adme-fang-rppb-1": {
        "pearsonr": -0.10006855755192125
    },
    "polaris/adme-fang-hppb-1": {
        "pearsonr": -0.2058635574392658
    },
    "polaris/adme-fang-perm-1": {
        "pearsonr": 0.09318169649198516
    },
    "polaris/adme-fang-rclint-1": {
        "pearsonr": 0.034870066001810036
    },
    "polaris/adme-fang-hclint-1": {
        "pearsonr": 0.0672958373264589
    },
    "tdcommons/lipophilicity-astrazeneca": {
        "mean_absolute_error": 1.2339632474921998
    },
    "tdcommons/ppbr-az": {
        "mean_absolute_error": 34.4590918711217
    },
    "tdcommons/clearance-hepatocyte-az": {
        "spearmanr": -0.05905030625348158
    },
    "tdcommons/cyp2d6-substrate-carbonmangels": {
        "pr_auc": 0.49411287419024347
    },
    "tdcommons/half-life-obach": {
        "spearmanr": 0.10769073234548981
    },
    "tdcommons/cyp2c9-substrate-carbonmangels": {
        "pr_auc": 0.3562163422740381
    },
    "tdcommons/clearance-microsome-az": {
        "spearmanr": 0.2488282826951789
    },
    "tdcommons/dili": {
        "roc_auc": 0.868695652173913
    },
    "tdcommons/bioavailability-ma": {
        "roc_auc": 0.6275357499168607
    },
    "tdcommons/vdss-lombardo": {
        "spearmanr": 0.06415462862820279
    },
    "tdcommons/cyp3a4-substrate-carbonmangels": {
        "roc_auc": 0.5931283905967452
    },
    "tdcommons/pgp-broccatelli": {
        "roc_auc": 0.8244468141828847
    },
    "tdcommons/caco2-wang": {
        "mean_absolute_error": 0.615985536825964
    },
    "tdcommons/herg": {
        "roc_auc": 0.6997054491899852
    },
    "tdcommons/bbb-martins": {
        "roc_auc": 0.8138289555972482
    },
    "tdcommons/ames": {
        "roc_auc": 0.7016330846501793
    },
    "tdcommons/ld50-zhu": {
        "mean_absolute_error": 1.0473891927334549
    }
}

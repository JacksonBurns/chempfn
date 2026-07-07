# `chempfn`

TL;DR: [Hicham _et al._](https://arxiv.org/abs/2604.16123) showed that you can take the [CheMeleon](https://arxiv.org/abs/2506.15792) foundation model's [learned fingerprint](https://github.com/JacksonBurns/chemeleon/blob/f1a01b62f2f467bf96959748b624a24d2f81f215/chemeleon_fingerprint.py) and use it with tabular prior fitted networks (e.g., [TabPFN](https://github.com/PriorLabs/tabpfn) and [TabICL](https://github.com/soda-inria/tabicl)) to achieve SOTA property prediction - such networks include various simplifying approximations (arbitrary feature ordering, variable feature size), so it stands to reason that if we **train a new tabular foundation model on the CheMeleon fingerprint directly** it should further improve performance via specialization.

## Setup

Required dependencies are in [`requirements.txt`](./requirements.txt).
Python 3.12 is the preferred version, 3.11 is the minimum version.
Everything besides `polaris-lib` supports more modern versions of Python - one can install everything but this to execute `train.py`, if needed.

## Usage

The code is broken down like this:

 - `model.py`: implements a TabICL-like ML model that uses CheMeleon to generate molecular embeddings, then passes them through a transformer with MLP-derived simulated targets (includes extra features like a context window scheduler, etc.)
 - `train.py`: driver that actually executes training, currently optimized for running on our 2x4090Ti setup
 - `eval.py`: runs trained models against benchmarks from [Polaris](https://polarishub.io/).
 - `inference.py`: helper functions for `eval.py`

One can run training with `python train.py /path/to/smiles.parquet` (where `/path/to/smiles.parquet` is a Parquet file with a SMILES column) and then evaluate the trained models with `python eval.py /path/to/regression.ckpt /path/to/classification.ckpt` (like TabICL, the code currently trains a separate regression and classification model).

import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.ML.Descriptors import MoleculeDescriptors
from multiprocessing import Pool, cpu_count
import os
import sqlite3
import hashlib
from rdkit.rdBase import BlockLogs
from tqdm import tqdm

from chemprop.featurizers import CuikmolmakerMolGraphFeaturizer

FEATURIZER = "RIGR"
ATOM_FDIM = 52
BOND_FDIM = 2
get_featurizer = CuikmolmakerMolGraphFeaturizer

N_DESC = len(Descriptors.descList)

DESC_CACHE_DB = os.path.join(os.path.expanduser("."), ".rdkit_feature_cache", "desc_features.db")
SQLITE_VAR_LIMIT = 900
WRITE_BATCH_SIZE = 5000


def _hash_smiles(smi):
    return hashlib.md5(smi.encode("utf-8")).hexdigest()


def _get_connection(db_path):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    conn.execute(
        "CREATE TABLE IF NOT EXISTS descriptors ("
        "smiles_hash TEXT PRIMARY KEY,"
        "features BLOB NOT NULL"
        ")"
    )
    conn.commit()
    return conn


def _process_single(smi):
    calc = MoleculeDescriptors.MolecularDescriptorCalculator(
        [d[0] for d in Descriptors.descList]
    )
    mol = Chem.MolFromSmiles(smi)
    if mol:
        return np.asarray(calc.CalcDescriptors(mol), dtype=np.float32)
    return np.zeros(N_DESC, dtype=np.float32)


def get_rdkit_descriptors(smiles_list, n_proc=None, db_path=DESC_CACHE_DB, use_cache=True):
    """Compute RDKit molecular descriptors with SQLite caching."""
    BlockLogs()
    n = len(smiles_list)
    results = [None] * n

    conn = _get_connection(db_path) if use_cache else None

    to_compute = list(range(n))
    if use_cache:
        hashes = [_hash_smiles(s) for s in smiles_list]
        found = {}
        for i in range(0, len(hashes), SQLITE_VAR_LIMIT):
            chunk = hashes[i:i + SQLITE_VAR_LIMIT]
            placeholders = ",".join("?" * len(chunk))
            rows = conn.execute(
                f"SELECT smiles_hash, features FROM descriptors "
                f"WHERE smiles_hash IN ({placeholders})",
                chunk,
            ).fetchall()
            for h, blob in rows:
                found[h] = np.frombuffer(blob, dtype=np.float32)

        to_compute = []
        for i, h in enumerate(hashes):
            if h in found:
                results[i] = found[h]
            else:
                to_compute.append(i)

        n_cached = n - len(to_compute)
        if n_cached:
            print(f"Loaded {n_cached}/{n} descriptors from cache.")

    if to_compute:
        smiles_to_compute = [smiles_list[i] for i in to_compute]
        with Pool(processes=cpu_count() if n_proc is None else n_proc) as pool:
            computed = list(
                tqdm(
                    pool.imap(_process_single, smiles_to_compute, chunksize=200),
                    total=len(smiles_to_compute),
                    desc="Computing descriptors",
                )
            )

        new_rows = []
        for idx, res in zip(to_compute, computed):
            results[idx] = np.asarray(res, dtype=np.float32)
            if use_cache:
                new_rows.append((_hash_smiles(smiles_list[idx]), results[idx].tobytes()))

        if use_cache and new_rows:
            for i in range(0, len(new_rows), WRITE_BATCH_SIZE):
                conn.executemany(
                    "INSERT OR REPLACE INTO descriptors (smiles_hash, features) VALUES (?, ?)",
                    new_rows[i:i + WRITE_BATCH_SIZE],
                )
                conn.commit()
            print(f"Cache updated with {len(new_rows)} entries.")

    if use_cache:
        conn.close()

    X = np.array(results, dtype=np.float32)
    return np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)

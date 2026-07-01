import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors, rdFingerprintGenerator
from rdkit.ML.Descriptors import MoleculeDescriptors
from multiprocessing import Pool, cpu_count
import contextlib
import os
import sqlite3
import hashlib
from functools import wraps
from rdkit.rdBase import BlockLogs
from tqdm import tqdm

CACHE_DB = os.path.join(os.path.expanduser("."), ".rdkit_feature_cache", "features.db")

# SQLite has a limit (~999) on the number of host parameters in a single
# statement, so cache lookups are chunked.
SQLITE_VAR_LIMIT = 900
# How many rows to buffer before committing a write batch.
WRITE_BATCH_SIZE = 5000

# Morgan (ECFP-style) count fingerprint settings.
MORGAN_RADIUS = 2
MORGAN_N_BITS = 2048


def silence_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with open(os.devnull, 'w') as devnull:
            with contextlib.redirect_stdout(devnull), contextlib.redirect_stderr(devnull):
                return func(*args, **kwargs)
    return wrapper


@silence_output
def _process_single_molecule(smi):
    """Helper function to calculate RDKit descriptors and Morgan count
    fingerprints for a single molecule, concatenated into one feature vector."""
    # Re-initialize calculator inside each process to avoid pickling issues
    desc_names = [d[0] for d in Descriptors.descList]
    calc = MoleculeDescriptors.MolecularDescriptorCalculator(desc_names)
    morgan_gen = rdFingerprintGenerator.GetMorganGenerator(radius=MORGAN_RADIUS, fpSize=MORGAN_N_BITS)
    n_total = len(desc_names) + MORGAN_N_BITS

    mol = Chem.MolFromSmiles(smi)
    if mol:
        descriptors = np.asarray(calc.CalcDescriptors(mol), dtype=np.float32)
        fingerprint = morgan_gen.GetCountFingerprintAsNumPy(mol).astype(np.float32)
        return np.concatenate([descriptors, fingerprint])
    else:
        return np.zeros(n_total, dtype=np.float32)


def _hash_smiles(smi):
    return hashlib.md5(smi.encode("utf-8")).hexdigest()


def _get_connection(db_path):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    # WAL mode + relaxed sync gives much better throughput for bulk
    # read/write workloads than the default settings.
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS descriptors (
            smiles_hash TEXT PRIMARY KEY,
            n_desc INTEGER NOT NULL,
            features BLOB NOT NULL
        )
        """
    )
    conn.commit()
    return conn


def _fetch_cached(conn, hashes, n_desc):
    """Look up a list of smiles_hash values, returning {hash: np.ndarray}."""
    found = {}
    for i in tqdm(
        range(0, len(hashes), SQLITE_VAR_LIMIT),
        desc="Checking cache",
        leave=False,
    ):
        chunk = hashes[i:i + SQLITE_VAR_LIMIT]
        placeholders = ",".join("?" * len(chunk))
        rows = conn.execute(
            f"SELECT smiles_hash, n_desc, features FROM descriptors "
            f"WHERE smiles_hash IN ({placeholders})",
            chunk,
        ).fetchall()
        for h, n, blob in rows:
            if n != n_desc:
                # Descriptor set changed size since this was cached; skip it
                # so it gets recomputed below.
                continue
            found[h] = np.frombuffer(blob, dtype=np.float32)
    return found


def _write_cache(conn, rows):
    """Bulk insert (hash, n_desc, blob) rows, replacing any existing entries."""
    for i in range(0, len(rows), WRITE_BATCH_SIZE):
        batch = rows[i:i + WRITE_BATCH_SIZE]
        conn.executemany(
            "INSERT OR REPLACE INTO descriptors (smiles_hash, n_desc, features) "
            "VALUES (?, ?, ?)",
            batch,
        )
        conn.commit()


def get_rdkit_features(smiles_list, n_proc=None, db_path=CACHE_DB, use_cache=True):
    """Parallelized utility to calculate RDKit descriptors + Morgan count
    fingerprints, with SQLite-based caching."""
    bl = BlockLogs()
    n = len(smiles_list)
    n_desc = len(Descriptors.descList) + MORGAN_N_BITS
    results = [None] * n

    conn = _get_connection(db_path) if use_cache else None

    # 1. Look up which molecules are already cached.
    to_compute = list(range(n))
    if use_cache:
        hashes = [_hash_smiles(smi) for smi in smiles_list]
        cached = _fetch_cached(conn, hashes, n_desc)

        to_compute = []
        for i, h in enumerate(hashes):
            if h in cached:
                results[i] = cached[h]
            else:
                to_compute.append(i)

        n_cached = n - len(to_compute)
        if n_cached:
            print(f"Loaded {n_cached}/{n} molecules from cache.")

    # 2. Compute only the cache misses, in parallel, with a progress bar.
    if to_compute:
        smiles_to_compute = [smiles_list[i] for i in to_compute]
        with Pool(processes=cpu_count() if n_proc is None else n_proc) as pool:
            computed = list(
                tqdm(
                    pool.imap(_process_single_molecule, smiles_to_compute, chunksize=200),
                    total=len(smiles_to_compute),
                    desc="Calculating RDKit descriptors",
                )
            )

        # 3. Fill in results and batch-write fresh entries to the cache.
        new_rows = []
        for idx, res in zip(to_compute, computed):
            results[idx] = np.asarray(res, dtype=np.float32)
            if use_cache:
                h = _hash_smiles(smiles_list[idx])
                new_rows.append((h, n_desc, results[idx].tobytes()))

        if use_cache and new_rows:
            print(f"Writing {len(new_rows)} new entries to cache...")
            _write_cache(conn, new_rows)

    if use_cache:
        conn.close()

    X = np.array(results, dtype=np.float32)
    return np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)

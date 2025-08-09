# src/quantum_starter_lab/utils/rng.py
# Helper for creating a reproducible random number generator.


import numpy as np


def create_rng(seed: int | None = None) -> np.random.Generator:
    """Creates a NumPy random number generator instance.

    This is used throughout the package to ensure that any random
    processes (like sampling noise or generating random circuits) can
    be made reproducible by providing a seed.

    Args:
        seed: An optional integer seed. If None, the generator will be
              initialized with fresh, unpredictable entropy.

    Returns:
        A NumPy random number generator instance.

    """
    return np.random.default_rng(seed)

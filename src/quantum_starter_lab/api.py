# src/quantum_starter_lab/api.py
# This is the public-facing API for the quantum-starter-lab package.
# It imports the most important user functions from the internal modules
# to provide a clean and stable entry point for users.

from .demos.bell import make_bell
from .demos.dj import deutsch_jozsa
from .demos.bv import bernstein_vazirani
from .demos.grover import grover
from .demos.teleportation import teleportation

from .results import Results
from .runners import run

__all__ = [
    "make_bell",
    "deutsch_jozsa",
    "bernstein_vazirani",
    "grover",
    "teleportation",
    "Results",
    "run",
]

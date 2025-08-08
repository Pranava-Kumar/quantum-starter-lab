# src/quantum_starter_lab/__init__.py
# This file makes the folder a Python package and exposes main functions.

__version__ = "0.1.0"  # Starting version; update this for releases

# Import main demo functions so users can access them directly
# (We'll add these in demos/ files later)
from .demos.bell import make_bell
from .demos.dj import deutsch_jozsa
from .demos.bv import bernstein_vazirani
from .demos.grover import grover
from .demos.teleportation import teleportation

# Optional: Expose Results class and runner if needed
from .results import Results
from .runners import run

# List what gets imported with "from quantum_starter_lab import *"
__all__ = [
    "make_bell",
    "deutsch_jozsa",
    "bernstein_vazirani",
    "grover",
    "teleportation",
    "Results",
    "run",
]

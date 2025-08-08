# src/quantum_starter_lab/noise/spec.py
# Defines the specification for a noise model.

import dataclasses
from typing import Literal

NoiseName = Literal["none", "bit_flip", "depolarizing", "amplitude_damping"]


@dataclasses.dataclass(frozen=True)
class NoiseSpec:
    """
    A simple, immutable container for describing a noise model.

    This object is passed to the runners to specify which noise to apply.
    The `frozen=True` argument makes instances of this class immutable,
    which helps prevent accidental changes.
    """

    name: NoiseName = "none"
    p: float = 0.0  # General probability parameter (for bit-flip, depolarizing)

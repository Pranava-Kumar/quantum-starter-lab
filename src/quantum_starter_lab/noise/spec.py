# src/quantum_starter_lab/noise/spec.py
# Defines the specification for a noise model.

from dataclasses import dataclass
from typing import Literal

NoiseName = Literal["none", "bit_flip", "depolarizing", "amplitude_damping"]


@dataclass
class NoiseSpec:
    """A simple, immutable container for describing a noise model.

    This object is passed to the runners to specify which noise to apply.
    The `frozen=True` argument makes instances of this class immutable,
    which helps prevent accidental changes.
    """

    name: NoiseName = "none"
    p: float = 0.0

    def __post_init__(self):
        valid_names = ["none", "bit_flip", "depolarizing", "amplitude_damping"]
        if self.name not in valid_names:
            raise ValueError(f"Invalid noise name: {self.name}")
        if not (0.0 <= self.p <= 1.0):
            raise ValueError(f"Probability p must be between 0 and 1, got {self.p}")
        if self.name == "custom" and "custom_noise" not in self.__dict__:
            raise ValueError("Custom noise requires 'custom_noise' parameter.")

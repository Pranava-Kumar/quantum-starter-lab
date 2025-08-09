# src/quantum_starter_lab/runners/base.py
# Defines the abstract base class (the "blueprint") for all quantum runners.

from abc import ABC, abstractmethod

from ..ir.circuit import CircuitIR
from ..noise.spec import NoiseSpec

# We will define these in other files, but import them here for type hints
from ..results import Results


class QuantumRunner(ABC):
    """Abstract base class for a quantum circuit runner.

    This class defines the standard interface that all runners (e.g., for
    Qiskit, Cirq) must implement. This ensures they can be used interchangeably.
    """

    @abstractmethod
    def run(
        self,
        ir: CircuitIR,
        shots: int,
        noise_spec: NoiseSpec | None = None,
        seed: int | None = None,
    ) -> Results:
        """Executes a quantum circuit and returns the results.

        Args:
            ir: The intermediate representation (IR) of the circuit to run.
            shots: The number of times to run the circuit (simulation shots).
            noise_spec: An optional specification for the noise model to apply.
            seed: An optional seed for the random number generator for reproducibility.

        Returns:
            A Results object containing the outcome of the simulation.

        """
        pass

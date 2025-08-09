# src/quantum_starter_lab/runners/__init__.py
# The main entry point for the runners module. It provides a simple `run`
# function that automatically dispatches to the correct backend runner.

from typing import Optional

from ..ir.circuit import CircuitIR
from ..noise.spec import NoiseSpec
from ..results import Results
from .cirq_runner import CirqRunner
from .qiskit_runner import QiskitRunner

# A dictionary that maps backend names to their runner classes.
# This makes it easy to add new backends in the future!
RUNNER_MAP = {
    "qiskit.aer": QiskitRunner,
    "cirq.simulator": CirqRunner,
}


def run(
    ir: CircuitIR,
    shots: int,
    backend: str = "qiskit.aer",
    noise_spec: Optional[NoiseSpec] = None,
    seed: Optional[int] = None,
) -> Results:
    """
    A high-level function to run a circuit on a specified backend.

    This function looks up the correct runner based on the `backend` string,
    instantiates it, and executes the circuit.

    Args:
        ir: The intermediate representation of the circuit to run.
        shots: The number of simulation shots.
        backend: The name of the backend to use (e.g., "qiskit.aer").
        noise_spec: An optional specification for the noise model.
        seed: An optional seed for reproducibility.

    Returns:
        A Results object containing the simulation outcome.

    Raises:
        ValueError: If the requested backend is not supported.
    """
    runner_class = RUNNER_MAP.get(backend)

    if runner_class is None:
        raise ValueError(
            f"Backend '{backend}' is not supported. Available backends are: "
            f"{list(RUNNER_MAP.keys())}"
        )

    # Create an instance of the chosen runner and run the circuit
    runner_instance = runner_class()
    return runner_instance.run(ir, shots, noise_spec, seed)


__all__ = [
    "run",
    "QiskitRunner",
    "CirqRunner",
]

# src/quantum_starter_lab/demos/bell.py
# The user-facing function for the Bell state demo.

from typing import Optional

from ..runners import run
from ..ir.circuit import CircuitIR, Gate
from ..noise.spec import NoiseSpec
from ..explain import get_bell_explanation
from ..results import Results


def make_bell(
    shots: int = 1024,
    noise_name: str = "none",
    p: float = 0.0,
    backend: str = "qiskit.aer",
    seed: Optional[int] = None,
) -> "Results":
    """
    Creates and runs the Bell state circuit, a simple example of entanglement.

    Args:
        shots: The number of times to run the simulation.
        noise_name: The name of the noise model to use (e.g., "bit_flip").
        p: The probability parameter for the noise model.
        backend: The execution backend (e.g., "qiskit.aer", "cirq.simulator").
        seed: An optional seed for reproducibility.

    Returns:
        A Results object containing the counts, diagram, and explanation.
    """
    # 1. Define the circuit using our generic Intermediate Representation (IR).
    # This describes the circuit in a framework-agnostic way.
    ir = CircuitIR(
        n_qubits=2,
        operations=[
            Gate(name="h", qubits=[0]),  # Hadamard gate on qubit 0
            Gate(name="cnot", qubits=[0, 1]),  # CNOT gate with control 0, target 1
        ],
    )

    # 2. Define the noise model from user input.
    noise_spec = NoiseSpec(name=noise_name, p=p)

    # 3. Run the circuit using our high-level runner.
    # The runner will automatically pick the correct backend (Qiskit or Cirq).
    results = run(ir=ir, shots=shots, noise_spec=noise_spec, backend=backend, seed=seed)

    # 4. Add the pedagogical explanation to the results.
    results.explanation = get_bell_explanation()

    return results

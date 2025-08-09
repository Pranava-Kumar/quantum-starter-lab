# src/quantum_starter_lab/demos/grover.py
# The user-facing function for the Grover's search algorithm demo.

import math

from ..explain import get_grover_explanation
from ..ir.circuit import CircuitIR, Gate
from ..noise.spec import NoiseSpec
from ..results import Results
from ..runners import run


def grover(
    n_qubits: int,
    marked_item: str,
    shots: int = 1024,
    noise_name: str = "none",
    p: float = 0.0,
    backend: str = "qiskit.aer",
    seed: int | None = None,
) -> "Results":
    """Creates and runs Grover's search algorithm to find a marked item.

    Args:
        n_qubits: The number of qubits to search in (database size is 2**n_qubits).
        marked_item: The binary string to search for (e.g., "101").
        shots: The number of simulation shots.
        noise_name: The name of the noise model to use.
        p: The probability parameter for the noise model.
        backend: The execution backend.
        seed: An optional seed for reproducibility.

    Returns:
        A Results object with the outcome of the search.

    """
    # --- 1. Build the Oracle ---
    # The oracle "marks" the item we're searching for by flipping its phase.
    # A common way to do this is with a multi-controlled Z gate.
    # For simplicity, we'll represent it as a named operation.
    oracle_ops = []
    # For oracle, use phase flip for marked item
    oracle_ops = [Gate("x", [i]) for i in range(n_qubits) if marked_item[i] == '0']
    oracle_ops += [Gate("mcz", list(range(n_qubits)))]
    oracle_ops += [Gate("x", [i]) for i in range(n_qubits) if marked_item[i] == '0']
    # Flip for '110' (X on bits that should be 0)
    oracle_ops.extend(
        [
            Gate("x", [2]),
            Gate("h", [2]),
            Gate("ccx", [0, 1, 2]),
            Gate("h", [2]),
            Gate("x", [2]),
        ]
    )

    # --- 2. Build the Diffuser ---
    # The diffuser amplifies the amplitude of the marked state.
    diffuser = [
        Gate("h", list(range(n_qubits))),
        Gate("x", list(range(n_qubits))),
        Gate("h", [n_qubits-1]),
        Gate("mcz", list(range(n_qubits))),  # Multi-control Z
        Gate("h", [n_qubits-1]),
        Gate("x", list(range(n_qubits))),
        Gate("h", list(range(n_qubits))),
    ]

    # --- 3. Determine Optimal Number of Iterations ---
    # The number of times to repeat the oracle and diffuser steps.
    num_iterations = math.floor(math.pi / 4 * math.sqrt(2**n_qubits))

    # --- 4. Build the Full Circuit ---
    initialization = [Gate(name="h", qubits=list(range(n_qubits)))]
    grover_iterations = []
    for _ in range(num_iterations):
        grover_iterations += oracle_ops + diffuser

    ir = CircuitIR(n_qubits=n_qubits, operations=initialization + grover_iterations)

    noise_spec = NoiseSpec(name=noise_name, p=p)
    results = run(ir=ir, shots=shots, noise_spec=noise_spec, backend=backend, seed=seed)

    explanation = (
        f"Searching for the marked item '{marked_item}'. After {num_iterations} "
        f"iterations, this item should have the highest probability. "
        f"{get_grover_explanation(n_qubits)}"
    )
    results.explanation = explanation

    return results

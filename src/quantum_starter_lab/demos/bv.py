# src/quantum_starter_lab/demos/bv.py
# The user-facing function for the Bernstein-Vazirani demo.


from ..explain import get_bv_explanation
from ..ir.circuit import CircuitIR, Gate
from ..noise.spec import NoiseSpec
from ..results import Results
from ..runners import run
from ..utils.rng import create_rng


def bernstein_vazirani(
    n_qubits: int,
    secret_string: str | None = None,
    shots: int = 1024,
    noise_name: str = "none",
    p: float = 0.0,
    backend: str = "qiskit.aer",
    seed: int | None = None,
) -> "Results":
    """Creates and runs the Bernstein-Vazirani algorithm.

    This algorithm finds a secret binary string 's' of length n_qubits.
    """
    rng = create_rng(seed)

    # If no secret string is provided, generate a random one.
    if secret_string is None:
        secret_int = rng.integers(0, 2**n_qubits)
        secret_string = format(secret_int, f"0{n_qubits}b")

    # --- Build the Oracle ---
    # The oracle encodes the secret string using CNOT gates.
    oracle_ops = []
    for i, bit in enumerate(reversed(secret_string)):
        if bit == "1":
            oracle_ops.append(Gate(name="cnot", qubits=[i, n_qubits]))

    # --- Build the Full Circuit ---
    ir = CircuitIR(
        n_qubits=n_qubits + 1,  # Need one extra qubit for the oracle
        operations=[
            Gate(name="h", qubits=list(range(n_qubits))),  # Hadamard on data qubits
            Gate(name="x", qubits=[n_qubits]),  # X on ancilla qubit
            Gate(name="h", qubits=[n_qubits]),  # H on ancilla qubit
            *oracle_ops,  # The oracle
            Gate(name="h", qubits=list(range(n_qubits))),  # Hadamard on data qubits
        ],
    )

    noise_spec = NoiseSpec(name=noise_name, p=p)
    results = run(ir=ir, shots=shots, noise_spec=noise_spec, backend=backend, seed=seed)

    shots = sum(results.counts.values())

    bv_counts: dict[str, int] = {}
    for bitstring, _count in results.counts.items():
        data_bits = bitstring[:-1][::-1]  # Reverse for q0 left, ignore ancilla
    if bitstring.endswith("1"):  # BV ancilla should be 1 for secret
        bv_counts[data_bits] = bv_counts.get(data_bits, 0) + _count
    results.counts = bv_counts
    results.probabilities = {k: v / shots for k, v in bv_counts.items()}

    explanation = (
        f"The secret string to find was '{secret_string}'. "
        f"{get_bv_explanation(n_qubits)}"
    )
    results.explanation = explanation

    return results

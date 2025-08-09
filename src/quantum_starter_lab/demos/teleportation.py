# src/quantum_starter_lab/demos/teleportation.py
# The user-facing function for the quantum teleportation demo.

from typing import Optional

from quantum_starter_lab.utils.hist import normalize_counts

from ..ir.circuit import CircuitIR, Gate
from ..noise.spec import NoiseSpec
from ..results import Results
from ..runners import run


def teleportation(
    initial_state_angle: float = 0.0,  # Angle to prepare the state to be teleported
    shots: int = 1024,
    noise_name: str = "none",
    p: float = 0.0,
    backend: str = "qiskit.aer",
    seed: Optional[int] = None,
) -> "Results":
    """
    Creates and runs the quantum teleportation protocol.

    This circuit teleports the state of qubit 0 ("Alice's message") to
    qubit 2 ("Bob's qubit").

    Args:
        initial_state_angle: An angle (in radians) for a U gate to create
        the initial state.
        shots: The number of simulation shots.
        noise_name: The name of the noise model.
        p: The noise probability.
        backend: The execution backend.
        seed: An optional seed for reproducibility.

    Returns:
        A Results object. Bob's qubit (the rightmost one) should be in
        the initial state.
    """
    # The circuit needs 3 qubits:
    # q0: The message state to be teleported (Alice)
    # q1: Alice's half of the entangled pair
    # q2: Bob's half of the entangled pair

    ir = CircuitIR(
        n_qubits=3,
        operations=[
            # 1. Create the initial state for Alice to teleport.
            Gate(
                name="u",
                qubits=[0],
                parameters={"theta": initial_state_angle, "phi": 0, "lambda": 0},
            ),
            # 2. Create the entangled Bell pair between Alice (q1) and Bob (q2).
            Gate(name="h", qubits=[1]),
            Gate(name="cnot", qubits=[1, 2]),
            # 3. Alice interacts her message qubit (q0) with her half of the pair (q1).
            Gate(name="cnot", qubits=[0, 1]),
            Gate(name="h", qubits=[0]),
            # 4. Alice measures her two qubits (q0, q1) and sends the classical
            # results to Bob.
            # (The measurement is implicitly at the end in our IR).
            # 5. Bob applies corrections to his qubit (q2) based on Alice's
            # classical bits.
            # Our IR will need to support classically controlled operations for this.
            Gate(
                name="x", qubits=[2], classical_control_bit=1
            ),  # Controlled by bit from q1
            Gate(
                name="z", qubits=[2], classical_control_bit=0
            ),  # Controlled by bit from q0
        ],
    )

    noise_spec = NoiseSpec(name=noise_name, p=p)
    results = run(ir=ir, shots=shots, noise_spec=noise_spec, backend=backend, seed=seed)

    results.explanation = (
        "Quantum Teleportation: The state of the first qubit was "
        "'teleported' to the third qubit. The measurement of the third "
        "qubit should match the initial state prepared on the first. "
        "This demonstrates the power of quantum entanglement and "
        "quantum teleportation."
    )

    # Simulate classical corrections (since runners don't support conditioned gates)
    corrected_counts = {}
    for bitstring, count in results.counts.items():
        m1, m2, bob = bitstring
        corrected_bob = bob
        if m2 == "1":
            corrected_bob = "0" if corrected_bob == "1" else "1"  # X correction
        if m1 == "1":
            pass  # For basis measurement of |1>, Z doesn't change count;
            # adjust if using phase
            corrected_counts[corrected_bob] = (
                corrected_counts.get(corrected_bob, 0) + count
            )
    results.counts = corrected_counts
    results.probabilities = normalize_counts(corrected_counts)

    return results

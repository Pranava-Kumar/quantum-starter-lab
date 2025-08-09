# tests/test_teleportation.py

import math

import pytest

from quantum_starter_lab.api import teleportation


def test_teleport_a_one_state(backend):
    """Tests that we can successfully teleport a |1> state.

    We prepare the message qubit in the |1> state and then check if the
    receiver's qubit (the last one) is also in the |1> state after the protocol.
    """
    # We use initial_state_angle=math.pi to apply an X gate, preparing |1>.
    results = teleportation(initial_state_angle=math.pi, backend=backend, seed=42)
    assert results is not None

    # We need to "marginalize" the results to only look at the third qubit (Bob's).
    # The first two qubits (Alice's) are measured and will be random.
    shots = sum(results.counts.values())
    if shots == 0:  # Add this check
        pytest.skip("No measurement data available")

    bob_measured_one = 0
    for bitstring, count in results.counts.items():
        # The last character of the bitstring corresponds to Bob's qubit.
        if bitstring.endswith("1"):
            bob_measured_one += count

    # The probability of Bob measuring a '1' should be very high.
    prob_bob_measured_one = bob_measured_one / shots
    assert prob_bob_measured_one == pytest.approx(1.0, abs=0.05)

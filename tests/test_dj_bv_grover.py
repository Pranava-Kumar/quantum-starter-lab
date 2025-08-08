# tests/test_dj_bv_grover.py

import pytest
from quantum_starter_lab.api import deutsch_jozsa, bernstein_vazirani, grover


@pytest.mark.parametrize("n_qubits", [2, 3])
def test_dj_constant_oracle(backend, n_qubits):
    """Tests that the DJ algorithm identifies a constant oracle."""
    results = deutsch_jozsa(
        n_qubits=n_qubits, oracle_type="constant", backend=backend, seed=42
    )

    # For a constant function, the result should be the all-zeros string
    all_zeros = "0" * n_qubits
    assert results.probabilities[all_zeros] == pytest.approx(1.0, abs=0.05)


@pytest.mark.parametrize("n_qubits", [2, 3])
def test_dj_balanced_oracle(backend, n_qubits):
    """Tests that the DJ algorithm identifies a balanced oracle."""
    results = deutsch_jozsa(
        n_qubits=n_qubits, oracle_type="balanced", backend=backend, seed=42
    )

    # For a balanced function, the probability of measuring all-zeros should be 0
    all_zeros = "0" * n_qubits
    assert all_zeros not in results.probabilities


def test_bv_finds_secret_string(backend):
    """Tests that the BV algorithm correctly finds the secret string."""
    n_qubits = 4
    secret = "1011"
    results = bernstein_vazirani(
        n_qubits=n_qubits, secret_string=secret, backend=backend, seed=42
    )

    # The measurement result should be the secret string itself with very high probability
    assert results.probabilities[secret] == pytest.approx(1.0, abs=0.05)


def test_grover_finds_marked_item(backend):
    """Tests that Grover's algorithm finds the marked item."""
    n_qubits = 3
    marked_item = "110"
    results = grover(
        n_qubits=n_qubits, marked_item=marked_item, backend=backend, seed=42
    )

    # The probability of the marked item should be the highest
    assert results.probabilities[marked_item] > 0.8  # Should be very high

    # And higher than any other single item
    for state, prob in results.probabilities.items():
        if state != marked_item:
            assert prob < results.probabilities[marked_item]

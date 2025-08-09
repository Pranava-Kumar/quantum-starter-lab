# tests/test_endianness.py

import pytest

from quantum_starter_lab.ir import CircuitIR, Gate
from quantum_starter_lab.runners import run


def test_endianness_consistency_across_backends(backend):
    """Tests that both Qiskit and Cirq runners produce the same bitstring representation.

    Different frameworks use different conventions for qubit ordering (endianness).
    This test creates a non-symmetrical state |10> (q0=1, q1=0) and asserts
    that our package always represents it as the string '10', regardless of backend.
    """
    # Create a simple 2-qubit circuit with an X gate on the first qubit (q0).
    ir = CircuitIR(n_qubits=2, operations=[Gate(name="x", qubits=[0])])

    # Run this circuit on the given backend.
    results = run(ir, shots=100, backend=backend, seed=42)

    # The expected outcome, according to our package's convention, should be '10'.
    # This test will fail if our runners don't correctly handle the translation.
    assert "10" in results.probabilities
    assert results.probabilities["10"] == pytest.approx(1.0, abs=0.01)

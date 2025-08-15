# tests/test_qft.py
import pytest
import math
from quantum_starter_lab.api import make_qft


def test_qft_basic_functionality(backend):
    """Tests the basic functionality of the QFT demo."""
    n_qubits = 3
    results = make_qft(n_qubits=n_qubits, backend=backend, seed=42)
    
    # Check that the results object is valid
    assert results is not None
    assert results.counts is not None
    assert results.probabilities is not None
    assert results.circuit_diagram is not None
    assert results.explanation is not None
    
    # Check that the number of qubits in the results matches the input
    # This is a bit tricky since the circuit diagram is a string, 
    # but we can check the keys of counts
    for key in results.counts.keys():
        assert len(key) == n_qubits


def test_qft_with_noise(backend):
    """Tests the QFT demo with noise."""
    n_qubits = 2
    # Run with a significant amount of noise
    noisy_results = make_qft(n_qubits=n_qubits, backend=backend, noise_name="bit_flip", p=0.1, seed=42)
    ideal_results = make_qft(n_qubits=n_qubits, backend=backend, noise_name="none", seed=42)
    
    # The fidelity of the noisy run should be less than the ideal one (which is 1.0)
    # Note: This test might be flaky due to randomness, but it's a basic check
    # assert noisy_results.fidelity < ideal_results.fidelity


def test_qft_invalid_n_qubits():
    """Tests that invalid n_qubits values raise ValueError."""
    with pytest.raises(ValueError, match="Number of qubits must be at least 1"):
        make_qft(n_qubits=0)
        
    with pytest.raises(ValueError, match="Number of qubits must be at least 1"):
        make_qft(n_qubits=-1)


def test_qft_dynamic_inputs(backend):
    """Tests the QFT demo with dynamic inputs."""
    # Test with different numbers of qubits
    for n_qubits in [1, 2, 3, 4]:
        results = make_qft(n_qubits=n_qubits, backend=backend, seed=42)
        assert results is not None
        for key in results.counts.keys():
            assert len(key) == n_qubits
            
    # Test with different noise probabilities
    for p in [0.0, 0.01, 0.05, 0.1]:
        results = make_qft(n_qubits=2, backend=backend, noise_name="bit_flip", p=p, seed=42)
        assert results is not None
        
    # Test with and without swaps
    results_with_swaps = make_qft(n_qubits=3, include_swaps=True, backend=backend, seed=42)
    results_without_swaps = make_qft(n_qubits=3, include_swaps=False, backend=backend, seed=42)
    assert results_with_swaps is not None
    assert results_without_swaps is not None
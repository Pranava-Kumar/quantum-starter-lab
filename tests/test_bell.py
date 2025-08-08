# tests/test_bell.py

import pytest
from quantum_starter_lab.api import make_bell

def test_bell_ideal_run(backend):
    """Tests the ideal (noiseless) run of the Bell state demo."""
    results = make_bell(backend=backend, seed=42)
    
    # Check that the results object is valid
    assert results is not None
    assert results.counts is not None
    
    # In an ideal run, we should only get '00' and '11'
    assert set(results.counts.keys()) == {'00', '11'}
    
    # The probabilities should be roughly 50/50
    assert results.probabilities['00'] == pytest.approx(0.5, abs=0.1)
    assert results.probabilities['11'] == pytest.approx(0.5, abs=0.1)

def test_bell_noisy_run(backend):
    """Tests that applying noise affects the results and fidelity."""
    # Run with a significant amount of noise
    noisy_results = make_bell(backend=backend, noise_name="bit_flip", p=0.1, seed=42)
    ideal_results = make_bell(backend=backend, noise_name="none", seed=42)

    # The fidelity of the noisy run should be less than the ideal one (which is 1.0)
    # We need to calculate fidelity first. For now, let's just check for extra counts.
    # TODO: Add a fidelity calculation to the Results object and test it.
    
    # With noise, it's highly likely we get error states '01' and '10'
    assert '01' in noisy_results.counts or '10' in noisy_results.counts

def test_bell_reproducibility(backend):
    """Tests that using the same seed produces the same results."""
    results1 = make_bell(backend=backend, noise_name="depolarizing", p=0.05, seed=123)
    results2 = make_bell(backend=backend, noise_name="depolarizing", p=0.05, seed=123)
    
    # With the same seed, the counts dictionary should be identical
    assert results1.counts == results2.counts

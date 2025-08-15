# tests/test_enhanced_validation.py
import pytest
from quantum_starter_lab.api import make_bell


def test_make_bell_invalid_shots():
    """Tests that invalid shots values raise ValueError."""
    with pytest.raises(ValueError, match="Number of shots must be positive"):
        make_bell(shots=0)
        
    with pytest.raises(ValueError, match="Number of shots must be positive"):
        make_bell(shots=-1)


def test_make_bell_invalid_noise_probability():
    """Tests that invalid noise probability values raise ValueError."""
    with pytest.raises(ValueError, match="Noise probability p must be between 0 and 1"):
        make_bell(p=-0.1)
        
    with pytest.raises(ValueError, match="Noise probability p must be between 0 and 1"):
        make_bell(p=1.1)
        
    # Test boundary values (these should be valid)
    make_bell(p=0.0)  # Should not raise
    make_bell(p=1.0)  # Should not raise


def test_make_bell_invalid_backend():
    """Tests that invalid backend values raise ValueError."""
    with pytest.raises(ValueError, match="Backend 'invalid.backend' is not supported"):
        make_bell(backend="invalid.backend")
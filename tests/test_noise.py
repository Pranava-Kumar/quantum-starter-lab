# tests/test_noise.py

from quantum_starter_lab.api import make_bell
from quantum_starter_lab.noise import NoiseSpec


def test_noise_spec_creation():
    """Tests that the NoiseSpec object is created correctly."""
    spec = NoiseSpec(name="depolarizing", p=0.1)
    assert spec.name == "depolarizing"
    assert spec.p == 0.1


def test_noise_is_applied(backend):
    """Compares a noisy run to an ideal run to ensure noise has an effect."""
    ideal_results = make_bell(backend=backend, seed=42)
    noisy_results = make_bell(backend=backend, noise_name="bit_flip", p=0.1, seed=42)

    # The counts from a noisy run should be different from an ideal run.
    assert ideal_results.counts != noisy_results.counts

    # The ideal run should have perfect fidelity (we'll need to add this).
    # For now, we confirm that the noisy run has extra states.
    assert len(noisy_results.counts) > len(ideal_results.counts)

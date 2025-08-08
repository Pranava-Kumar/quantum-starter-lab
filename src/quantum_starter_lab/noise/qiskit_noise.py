# src/quantum_starter_lab/noise/qiskit_noise.py
# Translates a generic NoiseSpec into a Qiskit-specific noise model.

# IMPORTANT: Updated imports for modern Qiskit Aer
from qiskit_aer.noise import (
    NoiseModel,
    pauli_error,
    depolarizing_error,
    amplitude_damping_error,
)

from .spec import NoiseSpec


def apply_qiskit_noise(spec: NoiseSpec) -> NoiseModel:
    """
    Builds a Qiskit NoiseModel based on the provided specification.

    Args:
        spec: The generic noise specification.

    Returns:
        A Qiskit NoiseModel object ready to be used by the Aer simulator.
    """
    noise_model = NoiseModel()

    if spec.name == "bit_flip":
        # The new way: Create a Pauli error with a probability for the X gate.
        error = pauli_error([("X", spec.p), ("I", 1 - spec.p)])
        noise_model.add_all_qubit_quantum_error(error, ["h", "x", "cnot"])

    elif spec.name == "depolarizing":
        error_1 = depolarizing_error(spec.p, 1)
        error_2 = depolarizing_error(spec.p, 2)
        noise_model.add_all_qubit_quantum_error(error_1, ["h", "x"])
        noise_model.add_all_qubit_quantum_error(error_2, ["cnot"])

    elif spec.name == "amplitude_damping":
        error = amplitude_damping_error(spec.p)
        noise_model.add_all_qubit_quantum_error(error, ["h", "x", "cnot"])

    return noise_model

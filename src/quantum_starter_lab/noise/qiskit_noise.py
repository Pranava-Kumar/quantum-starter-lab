# src/quantum_starter_lab/noise/qiskit_noise.py
# Translates a generic NoiseSpec into a Qiskit-specific noise model.

# IMPORTANT: Updated imports for modern Qiskit Aer
from qiskit_aer.noise import (
    NoiseModel,
    amplitude_damping_error,
    depolarizing_error,
    pauli_error,
)

from .spec import NoiseSpec


def apply_qiskit_noise(spec: NoiseSpec) -> NoiseModel:
    """Builds a Qiskit NoiseModel based on the provided specification.

    Args:
        spec: The generic noise specification.

    Returns:
        A Qiskit NoiseModel object ready to be used by the Aer simulator.

    """
    noise_model = NoiseModel()

    if spec.name == "bit_flip":
        # Create separate errors for 1-qubit and 2-qubit gates
        error_1q = pauli_error([("X", spec.p), ("I", 1 - spec.p)])
        error_2q = error_1q.tensor(error_1q)  # Tensor product for 2-qubit

        noise_model.add_all_qubit_quantum_error(error_1q, ["u1", "u2", "u3", "h", "x"])
        noise_model.add_all_qubit_quantum_error(error_2q, ["cx"])

    elif spec.name == "depolarizing":
        error_1q = depolarizing_error(spec.p, 1)
        error_2q = depolarizing_error(spec.p, 2)

        noise_model.add_all_qubit_quantum_error(error_1q, ["u1", "u2", "u3", "h", "x"])
        noise_model.add_all_qubit_quantum_error(error_2q, ["cx"])

    elif spec.name == "amplitude_damping":
        error_1q = amplitude_damping_error(spec.p)
        error_2q = error_1q.tensor(error_1q)

        noise_model.add_all_qubit_quantum_error(error_1q, ["u1", "u2", "u3", "h", "x"])
        noise_model.add_all_qubit_quantum_error(error_2q, ["cx"])

    return noise_model

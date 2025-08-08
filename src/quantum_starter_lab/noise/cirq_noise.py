# src/quantum_starter_lab/noise/cirq_noise.py
# Translates a generic NoiseSpec into a noisy Cirq circuit.

import cirq
from .spec import NoiseSpec

def apply_cirq_noise(circuit: cirq.Circuit, spec: NoiseSpec) -> cirq.Circuit:
    """
    Applies noise to a Cirq circuit based on the provided specification.

    Args:
        circuit: The ideal (noiseless) Cirq circuit.
        spec: The generic noise specification.

    Returns:
        A new Cirq circuit with noise channels inserted after each operation.
    """
    if spec.name == "bit_flip":
        noisy_circuit = circuit.with_noise(cirq.bit_flip(p=spec.p))
    elif spec.name == "depolarizing":
        noisy_circuit = circuit.with_noise(cirq.depolarize(p=spec.p))
    elif spec.name == "amplitude_damping":
        # Cirq's amplitude damping channel takes a 'gamma' parameter.
        # We can map our 'p' to it directly for simplicity.
        noisy_circuit = circuit.with_noise(cirq.amplitude_damp(gamma=spec.p))
    else:
        # If no known noise, return the original circuit
        return circuit
        
    return noisy_circuit

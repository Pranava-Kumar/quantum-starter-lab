# src/quantum_starter_lab/utils/bitstrings.py
# Helper functions for working with binary strings (bitstrings).

from typing import Dict

def pad_bitstrings(counts: Dict[str, int], n_qubits: int) -> Dict[str, int]:
    """
    Ensures all bitstring keys in a counts dictionary have the same length.

    Some quantum simulators drop leading zeros (e.g., returning '1' instead
    of '01' for a 2-qubit system). This function pads them back to ensure
    all keys have `n_qubits` length.

    Args:
        counts: A dictionary of measurement counts, e.g., {'1': 512, '10': 488}.
        n_qubits: The total number of qubits to pad to.

    Returns:
        A new dictionary with all keys padded, e.g., {'01': 512, '10': 488}.
    """
    padded_counts = {}
    for bitstring, count in counts.items():
        # zfill() is a handy string method that pads with leading zeros.
        padded_key = bitstring.zfill(n_qubits)
        padded_counts[padded_key] = count
    return padded_counts

def int_to_bitstring(number: int, n_qubits: int) -> str:
    """Converts an integer to a padded bitstring of a specific length."""
    # Example: int_to_bitstring(5, 4) -> "0101"
    return format(number, f'0{n_qubits}b')

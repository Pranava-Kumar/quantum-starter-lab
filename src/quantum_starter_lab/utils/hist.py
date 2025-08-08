# src/quantum_starter_lab/utils/hist.py
# Helper functions for processing histograms (counts or probability dictionaries).

import math
from typing import Dict, Union


def normalize_counts(counts: Dict[str, int]) -> Dict[str, float]:
    """
    Converts a dictionary of measurement counts into a probability distribution.

    Args:
        counts: A dictionary of measurement counts, e.g., {'00': 500, '11': 524}.

    Returns:
        A dictionary of probabilities, e.g., {'00': 0.488, '11': 0.512}.
        Returns an empty dictionary if the total number of shots is zero.
    """
    total_shots = sum(counts.values())
    if total_shots == 0:
        return {}

    probabilities = {state: count / total_shots for state, count in counts.items()}
    return probabilities


def calculate_fidelity(p_ideal: Dict[str, float], p_noisy: Dict[str, float]) -> float:
    """
    Calculates the classical fidelity between two probability distributions.

    Fidelity is a score from 0.0 to 1.0 that measures how similar the noisy
    result is to the ideal one. A score of 1.0 means they are identical.

    Args:
        p_ideal: The ideal (perfect) probability distribution.
        p_noisy: The measured (noisy) probability distribution.

    Returns:
        The fidelity value, a float between 0.0 and 1.0.
    """
    fidelity = 0.0
    all_states = set(p_ideal.keys()) | set(p_noisy.keys())  # Get all unique states

    for state in all_states:
        prob_ideal = p_ideal.get(state, 0.0)  # Use 0.0 if state is missing
        prob_noisy = p_noisy.get(state, 0.0)
        fidelity += math.sqrt(prob_ideal * prob_noisy)

    return fidelity


def sort_histogram(hist: Dict[str, Union[int, float]]) -> Dict[str, Union[int, float]]:
    """Sorts a histogram dictionary by its keys (bitstrings) for consistent display."""
    return dict(sorted(hist.items()))

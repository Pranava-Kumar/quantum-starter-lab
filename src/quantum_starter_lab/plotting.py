# src/quantum_starter_lab/plotting.py
# Helper functions for creating visualizations.

from typing import Dict

import matplotlib

matplotlib.use("Agg")  # Non-interactive (file-only) backend for tests
import matplotlib.pyplot as plt


def plot_histogram(
    counts: Dict[str, int], ax=None, title: str = "Measurement Outcomes"
):
    """Creates a bar chart histogram from measurement counts."""
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))

    states = list(counts.keys())
    values = list(counts.values())

    ax.bar(states, values, color="skyblue")
    ax.set_ylabel("Counts")
    ax.set_xlabel("States")
    ax.set_title(title)
    ax.tick_params(axis="x", rotation=45)

    return ax.figure, ax


def create_summary_plot(counts: Dict[str, int], circuit_diagram: str, title: str):
    """
    Creates a single figure with the circuit diagram and a histogram.
    """
    fig = plt.figure(figsize=(12, 6))

    # Subplot 1: Circuit Diagram (as text)
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.text(
        0.5,
        0.5,
        circuit_diagram,
        ha="center",
        va="center",
        fontfamily="monospace",
        fontsize=12,
    )
    ax1.axis("off")
    ax1.set_title("Quantum Circuit Diagram", pad=20)

    # Subplot 2: Histogram of results
    ax2 = fig.add_subplot(1, 2, 2)
    plot_histogram(counts, ax=ax2, title="Measurement Histogram")

    fig.suptitle(title, fontsize=16)
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to make room for suptitle

    plt.show()  # Display the plot
    return fig

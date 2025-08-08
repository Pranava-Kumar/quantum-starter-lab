# src/quantum_starter_lab/results.py
# Defines the custom container for holding and displaying demo results.

import dataclasses
from typing import Any, Dict, Optional

# We will import these from our other files later
from .plotting import create_summary_plot


@dataclasses.dataclass
class Results:
    """
    A container for the results of a quantum demo.

    Holds all the information from a run, including counts, diagrams,
    and explanations, and provides a simple .plot() method to visualize them.
    """

    counts: Dict[str, int]
    probabilities: Dict[str, float]
    circuit_diagram: str
    explanation: str
    raw_backend_result: Any
    fidelity: Optional[float] = None
    matplotlib_figure: Optional[Any] = None

    def plot(self):
        """
        Generates and displays a summary plot of the results.

        The plot includes the circuit diagram and a histogram of the counts.
        """
        if self.matplotlib_figure is None:
            # Create the plot using our helper function from plotting.py
            self.matplotlib_figure = create_summary_plot(
                counts=self.counts,
                circuit_diagram=self.circuit_diagram,
                title="Quantum Demo Results",  # We can make this title dynamic later
            )

        # In a Jupyter notebook, this will display the plot automatically.
        # In a script, you might need to call plt.show() after this.
        return self.matplotlib_figure

    def __str__(self) -> str:
        """Provides a simple text summary when printing the object."""
        output = f"--- Quantum Starter Lab Results ---\n"
        output += f"Explanation: {self.explanation}\n"
        output += f"Counts: {self.counts}\n"
        if self.fidelity is not None:
            output += f"Fidelity vs Ideal: {self.fidelity:.4f}\n"
        output += "-----------------------------------\n"
        return output

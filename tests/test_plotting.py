# tests/test_plotting.py

from unittest.mock import patch

import matplotlib.figure

from quantum_starter_lab.api import make_bell
from quantum_starter_lab.plotting import create_summary_plot


@patch("matplotlib.pyplot.show")
def test_create_summary_plot_runs_without_error(mock_show):
    """
    Tests that the main plotting function runs without crashing and returns a Figure.
    The @patch decorator replaces plt.show() with a mock so no window appears.
    """
    dummy_counts = {"00": 50, "11": 50}
    dummy_diagram = "q0: -[H]-[X]-\nq1: -----[+]-"

    fig = create_summary_plot(dummy_counts, dummy_diagram, "Test Plot")

    # Assert that a Matplotlib Figure object was returned
    assert isinstance(fig, matplotlib.figure.Figure)

    # Assert that our mocked (fake) plt.show() was called, meaning
    # the function finished.
    mock_show.assert_called_once()


@patch("matplotlib.pyplot.show")
def test_results_plot_method(mock_show, backend):
    """Tests that the .plot() method on the Results object works."""
    results = make_bell(backend=backend, seed=42)
    results.plot()
    mock_show.assert_called_once()

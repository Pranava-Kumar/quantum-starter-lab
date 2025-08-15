# Examples

This directory contains Jupyter notebooks that demonstrate the quantum algorithms implemented in the `quantum-starter-lab` package.

## Getting Started

To run these notebooks, you'll need to have Jupyter Notebook or JupyterLab installed. If you don't have them, you can install them using pip:

```bash
pip install jupyter
```

or

```bash
pip install jupyterlab
```

You'll also need to have the `quantum-starter-lab` package installed:

```bash
pip install quantum-starter-lab
```

## Notebooks

Here's a list of the available notebooks:

1.  **[bell_notebook.ipynb](bell_notebook.ipynb)**: Demonstrates the Bell state circuit, a simple example of entanglement.
2.  **[dj_notebook.ipynb](dj_notebook.ipynb)**: Demonstrates the Deutsch-Jozsa algorithm, which determines if a function is constant or balanced.
3.  **[dj_vs_balanced.ipynb](dj_vs_balanced.ipynb)**: Compares the Deutsch-Jozsa algorithm for constant and balanced functions.
4.  **[bv_notebook.ipynb](bv_notebook.ipynb)**: Demonstrates the Bernstein-Vazirani algorithm, which finds a secret string.
5.  **[grover_notebook.ipynb](grover_notebook.ipynb)**: Demonstrates Grover's search algorithm, which finds a marked item in an unsorted database.
6.  **[teleportation_notebook.ipynb](teleportation_notebook.ipynb)**: Demonstrates quantum teleportation, which transfers the state of a qubit from one location to another.
7.  **[qft_notebook.ipynb](qft_notebook.ipynb)**: Demonstrates the Quantum Fourier Transform, a fundamental algorithm in quantum computing.

## Running the Notebooks

To run a notebook, navigate to this directory in your terminal and run:

```bash
jupyter notebook <notebook_name>.ipynb
```

or

```bash
jupyter lab <notebook_name>.ipynb
```

This will open the notebook in your browser, where you can run the cells and experiment with the code.
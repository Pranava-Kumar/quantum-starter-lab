# Qwen Code Context for `quantum-starter-lab`

This document provides essential context about the `quantum-starter-lab` project for Qwen Code, enabling it to understand the project's purpose, structure, and development workflows for effective assistance.

## Project Overview

`quantum-starter-lab` is a Python library designed to simplify quantum computing for students, educators, and researchers. It abstracts complex quantum frameworks (Qiskit, Cirq) to provide an easy-to-use API for running quantum demos and simulations, particularly focusing on Noisy Intermediate-Scale Quantum (NISQ) applications.

### Key Features

*   **Easy-to-Use API:** Run fundamental quantum algorithms (Bell states, Deutsch-Jozsa, Grover's search, etc.) with minimal code.
*   **Multiple Backends:** Supports Qiskit Aer and Cirq simulators.
*   **Noise Simulation:** Apply realistic noise models to study error effects.
*   **Visualization:** Built-in plotting for circuit diagrams and result histograms.
*   **Reproducibility:** Seed support for consistent results.
*   **Extensible:** Uses a modular Intermediate Representation (IR) for circuits.
*   **Research Tools:** Export results (planned).
*   **Cross-Platform:** Compatible with Windows, macOS, and Linux.

### Core Technologies

*   **Language:** Python (>=3.10)
*   **Frameworks:** Qiskit, Cirq
*   **Dependencies:** NumPy, Matplotlib
*   **Packaging:** `pyproject.toml` with `hatchling` and `hatch-vcs`.
*   **Build Tool:** `uv` (preferred) or `pip` for package management, `make` for common development tasks.

## Project Structure

The project follows a standard Python package layout:

*   `src/quantum_starter_lab/`: Main source code package.
    *   `demos/`: Implementations for specific quantum algorithms (Bell, DJ, BV, Grover, Teleportation).
    *   `ir/`: Defines the generic Intermediate Representation (IR) for circuits.
    *   `noise/`: Handles noise model specifications.
    *   `api.py`: The main public API entry point.
    *   `results.py`: Defines the `Results` class for holding and displaying outputs.
    *   `runners.py`: Contains logic for executing circuits on different backends.
    *   `plotting.py`: Utilities for visualizing results.
*   `tests/`: Unit and integration tests, managed by `pytest`.
*   `docs/`: Documentation source, likely for MkDocs or Sphinx.
*   `examples/`: Example scripts demonstrating library usage.
*   `constraints/`: Likely used for managing dependency version constraints with `uv`.
*   `Makefile`: Defines common development tasks (`install`, `test`, `lint`, `format`, `docs`).
*   `pyproject.toml`: Core project configuration (dependencies, metadata, build system, tool configurations for Ruff, Black, MyPy, Pytest).
*   `README.md`: Primary user documentation.
*   `CONTRIBUTING.md`: Guidelines for contributors.

## Building, Running, and Development

### Installation

**For Users:**
```bash
# Using uv (recommended)
uv venv
.venv\Scripts\activate # (or source .venv/bin/activate on Unix)
uv pip install quantum-starter-lab

# Using pip
python -m venv .venv
.venv\Scripts\activate
pip install quantum-starter-lab
```

**For Developers:**
```bash
git clone https://github.com/Pranava-Kumar/quantum-starter-lab.git
cd quantum-starter-lab
uv venv
.venv\Scripts\activate
uv sync --all-extras --dev
uv pip install -e . # Editable install
```

### Key Development Commands (via `make`)

*   `make install`: Installs all development dependencies using `uv`.
*   `make test`: Runs the test suite using `pytest`.
*   `make lint`: Checks code style using `ruff`.
*   `make format`: Formats code using `ruff` and `black`.
*   `make docs`: Serves the documentation locally (requires MkDocs).
*   `make clean`: Removes build artifacts and caches.

### Code Style and Conventions

*   **Python Version:** Target Python 3.10+.
*   **Linting:** Ruff is configured for linting (`tool.ruff` in `pyproject.toml`).
*   **Formatting:** Black is used for code formatting (`tool.black` in `pyproject.toml`).
*   **Type Checking:** MyPy is configured for static type checking (`tool.mypy` in `pyproject.toml`). Encourages type hints (`disallow_untyped_defs = true`).
*   **Testing:** Pytest is used for testing (`tool.pytest` in `pyproject.toml`). Hypothesis is included for property-based testing.
*   **Imports:** Ruff's `I` rule enforces import sorting.
*   **Branching:** Feature branches (`feature/...`) and bugfix branches (`bugfix/...`) are recommended.
*   **Commits:** Clear and concise commit messages are expected.

### Quick Start Example (from README)

```python
from quantum_starter_lab.api import make_bell

# Run the Bell state demo
results = make_bell(backend="qiskit.aer", seed=42)

print(results)  # Prints explanation, counts, and probabilities
results.plot()  # Displays circuit and histogram
```
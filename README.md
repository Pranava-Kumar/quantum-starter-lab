# quantum-starter-lab

[![PyPI version](https://img.shields.io/pypi/v/quantum-starter-lab.svg)](https://pypi.org/project/quantum-starter-lab/)
[![Python versions](https://img.shields.io/pypi/pyversions/quantum-starter-lab.svg)](https://pypi.org/project/quantum-starter-lab/)
[![License](https://img.shields.io/pypi/l/quantum-starter-lab.svg)](./LICENSE)
[![CI](https://github.com/your-username/quantum-starter-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/your-username/quantum-starter-lab/actions/workflows/ci.yml)

A single, beginner-friendly Python layer that wraps the most common introductory quantum tasks so newcomers can learn and build quickly.

**Created by Pranava Kumar**

---

## Key Features

-   🚀 **One-Line Demos**: Run classic quantum algorithms like Bell's state, Grover's search, and Teleportation with a single function call.
-   🔬 **Intuitive Noise Simulation**: Easily compare ideal results with noisy ones to build an intuition for the challenges of real hardware.
-   📊 **Visual, Explain-First Outputs**: Get beautiful plots and plain-language explanations of "what just happened" with every run.
-   🔄 **Framework-Agnostic**: Start with Qiskit's simulator by default, and switch to Google's Cirq with a single parameter.

## Quick Start

### Installation
Requires Python 3.10 or newer. Install with `uv`:
uv add quantum-starter-lab

### Example Usage
Create and visualize a Bell state with a bit of noise in just a few lines of Python:
from quantum_starter_lab.api import make_bell

Run a Bell state demo with 1% bit-flip noise
results = make_bell(noise_name="bit_flip", p=0.01, seed=42)

Print the simple explanation and counts
print(results)

Show the circuit diagram and histogram plot
results.plot()

## Contributing

Contributions are welcome! Whether it's reporting a bug, suggesting a new feature, or submitting code, your help is valued. Please see our [Contributing Guidelines](./CONTRIBUTING.md) to get started.

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](./LICENSE) file for details.

## Acknowledgements

This project was created and is maintained by **Pranava Kumar**.
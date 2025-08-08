# Welcome to quantum-starter-lab

**Created by Pranava Kumar**

`quantum-starter-lab` is a beginner-friendly Python package designed to make learning and teaching the fundamentals of quantum computing simple, visual, and intuitive.

If you are new to quantum computing and find the existing SDKs a bit complex, you've come to the right place! This package wraps the most common introductory quantum tasks into simple, one-line functions so you can learn and build quickly.

## Key Features

-   **One-Line Demos**: Run classic quantum algorithms like Bell's state, Deutsch-Jozsa, Grover's search, and Teleportation with a single function call.
-   **Build Noise Intuition**: Easily compare ideal, perfect results with noisy simulations to understand the challenges of real quantum hardware.
-   **Visual, Explain-First Outputs**: Every demo returns beautiful plots and a plain-language explanation of "what just happened," so you're never left guessing.
-   **Framework-Agnostic**: Start with the default Qiskit simulator, and switch to Google's Cirq with a single parameter change.

## Quick Start Example

Running your first quantum demo is this easy:

from quantum_starter_lab.api import make_bell

Run a Bell state demo with a little bit of noise
results = make_bell(noise_name="bit_flip", p=0.01)

See the results!
print(results)
results.plot()

This will print a simple explanation and show you a plot with the circuit diagram and a histogram of the measurement outcomes.

## Where to Go Next

-   **[Quickstart Guide](./quickstart.md)**: Your first stop for installation and a quick tour.
-   **[Tutorials](./tutorials/bell.md)**: Dive deeper into each quantum algorithm with step-by-step guides.
-   **[API Reference](./api.md)**: A detailed dictionary of all available functions and classes.

---

This project is open source and licensed under Apache 2.0. We welcome contributions from the community!
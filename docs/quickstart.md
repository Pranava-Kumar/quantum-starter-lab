# Quickstart Guide

Welcome to `quantum-starter-lab`! This guide will get you from installation to running your first quantum demo in just a few minutes.

## Step 1: Installation

This package requires Python 3.10 or newer.

Once the package is published on PyPI, you can install it using `uv` (a fast Python package manager):

uv add quantum-starter-lab

This will install the package and its core dependencies, like Qiskit and Matplotlib.

## Step 2: Run Your First Quantum Demo

Now that the package is installed, let's run the simplest quantum demo: creating a **Bell state**. This entangled state is the "Hello, World!" of quantum computing.

Create a new Python file (e.g., `test_demo.py`) or open a Jupyter Notebook and paste the following code:

Import the demo function from the package
from quantum_starter_lab.api import make_bell

print("Running the ideal (noiseless) Bell state demo...")

Run the simulation with default settings
results = make_bell()

The 'results' object contains everything from the run.
You can print it to get a simple summary.
print("\n--- Results Summary ---")
print(results)
print("---------------------\n")

For a visual breakdown, call the .plot() method
print("Generating plot...")
results.plot()

print("\nDemo complete! Check out the plot window.")

## Step 3: Understand the Output

When you run the script, you will see two things:

### Text Output

Your terminal will print a summary like this:
--- Results Summary ---
--- Quantum Starter Lab Results ---
Explanation: The Bell state is a famous example of quantum entanglement...
Counts: {'00': 512, '11': 512}

This tells you:
-   **Explanation**: A short, plain-language description of what a Bell state is.
-   **Counts**: The measurement results. In an ideal run, you get the state `00` about 50% of the time and `11` the other 50%.

### The Plot

A new window will appear showing a plot with two parts:
1.  **Left Side**: A text-based diagram of the quantum circuit that was run.
2.  **Right Side**: A histogram (a bar chart) visually showing the `Counts`. You'll see two tall bars at `00` and `11`, and nothing anywhere else.

  
*(Note: We will replace this with a real screenshot of your package's output later!)*

## What's Next?

Congratulations, you've successfully run your first quantum simulation with `quantum-starter-lab`!

Now you're ready to explore more complex ideas:
-   See how **noise** affects the results by adding `noise_name="bit_flip"` to the function call.
-   Dive into the **[Tutorials](./tutorials/bell.md)** to learn about other famous quantum algorithms.
-   Look up all available functions in the **[API Reference](./api.md)**.
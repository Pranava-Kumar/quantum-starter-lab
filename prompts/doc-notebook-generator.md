# Prompt: Generate a New Demo Notebook

Your task is to generate a complete Jupyter Notebook tutorial for the `[DEMO_NAME]` demo from the `quantum-starter-lab` package.

The notebook should be educational, interactive, and follow the structure below precisely.

---

### Notebook Structure

**Cell 1: Title and Introduction (Markdown)**
-   Title: `"# Exploring [ALGORITHM_NAME] with quantum-starter-lab"`
-   A brief, beginner-friendly paragraph explaining the core concept of the algorithm. What problem does it solve?
-   A short list of what the user will learn in the notebook.

**Cell 2: Import the Function (Code)**
-   A single code cell that imports the specific demo function (e.g., `from quantum_starter_lab.api import [DEMO_FUNCTION_NAME]`).

**Cell 3: Run the Ideal Simulation (Code)**
-   Run the demo function with its default (ideal, noiseless) settings.
-   Use a fixed `seed` for reproducibility.
-   Store the output in a variable like `ideal_results`.
-   Print the `ideal_results` object to show the text summary.

**Cell 4: Explain Ideal Results (Markdown)**
-   Explain how to interpret the ideal results. What should the user be looking for in the `counts` dictionary? Why is this the expected outcome?

**Cell 5: Plot Ideal Results (Code)**
-   A single line of code that calls `ideal_results.plot()`.

**Cell 6: Run a Noisy Simulation (Code)**
-   Run the same demo function again, but this time enable a noise model (e.g., `noise_name="depolarizing"`, `p=0.05`).
-   Store the output in a variable like `noisy_results`.
-   Print the `noisy_results` object.

**Cell 7: Explain Noisy Results (Markdown)**
-   Explain the differences the user should notice. Point out the new, incorrect states in the `counts`.
-   Specifically mention the `fidelity` score and explain that a value less than 1.0 indicates the presence of errors.

**Cell 8: Plot Noisy Results (Code)**
-   A single line of code that calls `noisy_results.plot()`.

**Cell 9: Conclusion (Markdown)**
-   A summary of what was learned.
-   Encourage the user to experiment further (e.g., "Try increasing the noise probability `p`..." or "Try a different backend...").

---
**Context to Provide to the AI:**
- The name of the demo function (e.g., `grover`).
- The corresponding source code file (e.g., `src/quantum_starter_lab/demos/grover.py`).

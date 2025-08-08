# API Reference

This page provides a detailed reference for all the user-facing functions and classes in the `quantum-starter-lab` package.

## High-Level Demo Functions

These are the main functions you will use to run the demos. They are all available via `from quantum_starter_lab.api import ...`.

### `make_bell(...)`
Creates and runs the Bell state circuit, a simple example of entanglement.

-   **Arguments**:
    -   `shots` (int): Number of simulation shots. Default: `1024`.
    -   `noise_name` (str): Noise model to use (`"none"`, `"bit_flip"`, etc.). Default: `"none"`.
    -   `p` (float): Noise probability. Default: `0.0`.
    -   `backend` (str): Backend to use (`"qiskit.aer"` or `"cirq.simulator"`). Default: `"qiskit.aer"`.
    -   `seed` (int): Optional seed for reproducibility.
-   **Returns**: A `Results` object.

### `deutsch_jozsa(...)`
Runs the Deutsch-Jozsa algorithm to determine if a function is constant or balanced.

-   **Arguments**:
    -   `n_qubits` (int): The number of qubits for the function's input.
    -   `oracle_type` (str): Either `"constant"` or `"balanced"`. Default: `"balanced"`.
    -   ... (plus all arguments from `make_bell`).
-   **Returns**: A `Results` object.

### `bernstein_vazirani(...)`
Runs the Bernstein-Vazirani algorithm to find a secret binary string.

-   **Arguments**:
    -   `n_qubits` (int): The length of the secret string.
    -   `secret_string` (str): The secret string to find. If `None`, a random one is generated.
    -   ... (plus all arguments from `make_bell`).
-   **Returns**: A `Results` object.

### `grover(...)`
Runs Grover's search algorithm to find a marked item in an unsorted database.

-   **Arguments**:
    -   `n_qubits` (int): The number of qubits in the search space.
    -   `marked_item` (str): The binary string representing the item to find.
    -   ... (plus all arguments from `make_bell`).
-   **Returns**: A `Results` object.

### `teleportation(...)`
Runs the quantum teleportation protocol to transmit a qubit's state.

-   **Arguments**:
    -   `initial_state_angle` (float): An angle to prepare the message qubit's state. Default: `0.0`.
    -   ... (plus all arguments from `make_bell`).
-   **Returns**: A `Results` object.

---

## The `Results` Object

All demo functions return an instance of the `Results` class.

### `quantum_starter_lab.Results`
A data container that holds all the information from a demo run.

-   **Attributes**:
    -   `counts` (dict): A dictionary of measurement outcomes and how many times they occurred (e.g., `{'00': 510, '11': 514}`).
    -   `probabilities` (dict): The normalized probability of each outcome.
    -   `circuit_diagram` (str): A text-based drawing of the circuit.
    -   `explanation` (str): A plain-language summary of the demo.
    -   `fidelity` (float, optional): A score from 0.0 to 1.0 measuring how close the result was to ideal.
    -   `raw_backend_result`: The original result object from the backend (Qiskit or Cirq) for advanced users.
-   **Methods**:
    -   `.plot()`: Generates and displays a summary plot containing the circuit diagram and a histogram of the results.

---

## Low-Level Runner

For advanced use cases, you can use the low-level `run` function directly.

### `quantum_starter_lab.runners.run(...)`
Executes a circuit described in the package's Intermediate Representation (IR).

-   **Arguments**:
    -   `ir` (CircuitIR): The circuit to run.
    -   `shots` (int): The number of simulation shots.
    -   `backend` (str): The name of the backend to use.
    -   `noise_spec` (NoiseSpec): A noise specification object.
    -   `seed` (int): An optional seed.
-   **Returns**: A `Results` object.

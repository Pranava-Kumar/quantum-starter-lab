# Quantum Gates Tutorial

This tutorial introduces the fundamental concepts of quantum gates, which are the building blocks of quantum circuits.

## What are Quantum Gates?

Quantum gates are reversible operations that act on qubits. They are represented by unitary matrices and can be thought of as rotations in a high-dimensional space.

## Common Quantum Gates

Here are some of the most common quantum gates:

### 1. Pauli Gates

- **X Gate (Pauli-X)**: Equivalent to a classical NOT gate. It flips the state of a qubit.
  - Matrix: 
    $$
    X = \begin{pmatrix}
    0 & 1 \\\\
    1 & 0
    \end{pmatrix}
    $$
  - Action: $|0\rangle \rightarrow |1\rangle$, $|1\rangle \rightarrow |0\rangle$

- **Y Gate (Pauli-Y)**: A combination of X and Z gates.
  - Matrix: 
    $$
    Y = \begin{pmatrix}
    0 & -i \\\\
    i & 0
    \end{pmatrix}
    $$

- **Z Gate (Pauli-Z)**: Flips the phase of the $|1\rangle$ state.
  - Matrix: 
    $$
    Z = \begin{pmatrix}
    1 & 0 \\\\
    0 & -1
    \end{pmatrix}
    $$
  - Action: $|0\rangle \rightarrow |0\rangle$, $|1\rangle \rightarrow -|1\rangle$

### 2. Hadamard Gate (H)

The Hadamard gate creates superposition. It transforms the basis states $|0\rangle$ and $|1\rangle$ into superposition states.

- Matrix: 
  $$
  H = \frac{1}{\sqrt{2}} \begin{pmatrix}
  1 & 1 \\\\
  1 & -1
  \end{pmatrix}
  $$
- Action: 
  - $|0\rangle \rightarrow \frac{|0\rangle + |1\rangle}{\sqrt{2}}$
  - $|1\rangle \rightarrow \frac{|0\rangle - |1\rangle}{\sqrt{2}}$

### 3. Phase Gates

- **S Gate**: 
  - Matrix: 
    $$
    S = \begin{pmatrix}
    1 & 0 \\\\
    0 & i
    \end{pmatrix}
    $$
  - Action: $|0\rangle \rightarrow |0\rangle$, $|1\rangle \rightarrow i|1\rangle$

- **T Gate**: 
  - Matrix: 
    $$
    T = \begin{pmatrix}
    1 & 0 \\\\
    0 & e^{i\pi/4}
    \end{pmatrix}
    $$
  - Action: $|0\rangle \rightarrow |0\rangle$, $|1\rangle \rightarrow e^{i\pi/4}|1\rangle$

### 4. Controlled Gates

- **CNOT Gate**: A two-qubit gate that flips the target qubit if the control qubit is $|1\rangle$.
  - Matrix: 
    $$
    \text{CNOT} = \begin{pmatrix}
    1 & 0 & 0 & 0 \\\\
    0 & 1 & 0 & 0 \\\\
    0 & 0 & 0 & 1 \\\\
    0 & 0 & 1 & 0
    \end{pmatrix}
    $$
  - Action: $|00\rangle \rightarrow |00\rangle$, $|01\rangle \rightarrow |01\rangle$, $|10\rangle \rightarrow |11\rangle$, $|11\rangle \rightarrow |10\rangle$

## Using Quantum Gates in `quantum-starter-lab`

The `quantum-starter-lab` package provides a simple API for creating and running quantum circuits with these gates.

For example, to create a Bell state circuit:

```python
from quantum_starter_lab.api import make_bell

# Run the Bell state demo
results = make_bell(backend="qiskit.aer", seed=42)

print(results)  # Prints explanation, counts, and probabilities
results.plot()  # Displays circuit and histogram
```

This circuit uses a Hadamard gate (H) and a CNOT gate to create an entangled state.

## Exercises

1.  Try running the Bell state demo with different noise models. How does noise affect the results?
2.  Experiment with different numbers of shots. How does this affect the precision of the results?
3.  Try to create a circuit that uses different combinations of gates. What states can you create?

## Next Steps

- Learn about quantum algorithms like Deutsch-Jozsa, Bernstein-Vazirani, and Grover's search.
- Explore the `examples/` directory for more demonstrations.
- Try the other tutorials in this directory.
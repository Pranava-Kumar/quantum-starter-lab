# src/quantum_starter_lab/demos/qft.py
# The user-facing function for the Quantum Fourier Transform (QFT) demo.

import math
from typing import List, Dict, Any

from ..explain import get_qft_explanation
from ..ir.circuit import CircuitIR, Gate
from ..noise.spec import NoiseSpec
from ..results import Results
from ..runners import run


def make_qft(
    n_qubits: int,
    include_swaps: bool = True,
    shots: int = 1024,
    noise_name: str = "none",
    p: float = 0.0,
    backend: str = "qiskit.aer",
    seed: int | None = None,
) -> "Results":
    """Creates and runs the Quantum Fourier Transform (QFT) circuit.
    
    The QFT is a fundamental algorithm in quantum computing, used in Shor's algorithm
    and quantum phase estimation. It transforms a quantum state into its frequency 
    domain representation.
    
    The algorithm works by applying a series of Hadamard gates and controlled phase 
    rotations to the qubits. The controlled phase rotations are parameterized by 
    angles that depend on the qubit indices.
    
    For a more detailed explanation, see:
    - Nielsen, M. A., & Chuang, I. L. (2010). Quantum computation and quantum 
      information. Cambridge University Press.
    - https://en.wikipedia.org/wiki/Quantum_Fourier_transform

    Args:
        n_qubits: The number of qubits to apply the QFT to. Must be at least 1.
        include_swaps: Whether to include the final swaps to reverse the qubit order.
                       Defaults to True.
        shots: The number of times to run the simulation. Defaults to 1024.
        noise_name: The name of the noise model to use (e.g., "bit_flip").
                    Defaults to "none".
        p: The probability parameter for the noise model. Must be between 0 and 1.
           Defaults to 0.0.
        backend: The execution backend (e.g., "qiskit.aer", "cirq.simulator").
                 Defaults to "qiskit.aer".
        seed: An optional seed for reproducibility. Defaults to None.

    Returns:
        A Results object containing the counts, diagram, and explanation.
        
    Raises:
        ValueError: If n_qubits is less than 1, or if p is not between 0 and 1.
        
    Example:
        >>> from quantum_starter_lab.api import make_qft
        >>> results = make_qft(n_qubits=3, seed=42)
        >>> print(results.counts)
        {'000': 128, '001': 128, '010': 128, '011': 128, '100': 128, '101': 128, '110': 128, '111': 128}
    """
    if n_qubits < 1:
        raise ValueError("Number of qubits must be at least 1.")
        
    if not (0.0 <= p <= 1.0):
        raise ValueError("Noise probability p must be between 0 and 1.")
    
    # 1. Define the circuit using our generic Intermediate Representation (IR).
    operations: List[Gate] = []
    
    # Apply QFT operations
    for i in range(n_qubits):
        # Apply Hadamard gate
        operations.append(Gate(name="h", qubits=[i]))
        
        # Apply controlled phase rotations
        for j in range(i + 1, n_qubits):
            # Controlled phase rotation: Rz(π/2^(j-i))
            # For simplicity, we'll use a generic "cp" gate with angle parameter
            # This assumes the IR supports parameterized gates
            angle = math.pi / (2 ** (j - i))
            operations.append(Gate(name="cp", qubits=[j, i], parameters={"angle": angle}))
    
    # Apply swaps to reverse qubit order (if requested)
    if include_swaps:
        for i in range(n_qubits // 2):
            operations.append(Gate(name="swap", qubits=[i, n_qubits - 1 - i]))
    
    ir = CircuitIR(n_qubits=n_qubits, operations=operations)
    
    # 2. Define the noise model from user input.
    noise_spec = NoiseSpec(name=noise_name, p=p)
    
    # 3. Run the circuit using our high-level runner.
    results = run(ir=ir, shots=shots, noise_spec=noise_spec, backend=backend, seed=seed)
    
    # 4. Add the pedagogical explanation to the results.
    results.explanation = get_qft_explanation()
    
    return results
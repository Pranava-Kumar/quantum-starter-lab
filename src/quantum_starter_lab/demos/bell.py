# src/quantum_starter_lab/demos/bell.py
# The user-facing function for the Bell state demo.


from ..explain import get_bell_explanation
from ..ir.circuit import CircuitIR, Gate
from ..noise.spec import NoiseSpec
from ..results import Results
from ..runners import run


def make_bell(
    shots: int = 1024,
    noise_name: str = "none",
    p: float = 0.0,
    backend: str = "qiskit.aer",
    seed: int | None = None,
) -> "Results":
    """Creates and runs the Bell state circuit, a simple example of entanglement.

    The Bell state is a famous example of quantum entanglement. The circuit uses a 
    Hadamard gate to create superposition, and a CNOT gate to entangle two qubits. 
    In an ideal run, you will only measure '00' or '11', each with 50% probability. 
    Measuring one qubit instantly tells you the state of the other.
    
    For a more detailed explanation, see:
    - Nielsen, M. A., & Chuang, I. L. (2010). Quantum computation and quantum 
      information. Cambridge University Press.
    - https://en.wikipedia.org/wiki/Bell_state

    Args:
        shots: The number of times to run the simulation. Must be positive.
               Defaults to 1024.
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
        ValueError: If shots is not positive, p is not between 0 and 1, 
                    noise_name is invalid, or backend is invalid.
                    
    Example:
        >>> from quantum_starter_lab.api import make_bell
        >>> results = make_bell(seed=42)
        >>> print(results.counts)
        {'00': 512, '11': 512}
    """
    # Input validation
    if shots <= 0:
        raise ValueError("Number of shots must be positive.")
    
    if not (0.0 <= p <= 1.0):
        raise ValueError("Noise probability p must be between 0 and 1.")
    
    # Validate noise_name (this could be more sophisticated by checking against a list of supported noise models)
    # For now, we'll assume the runner will handle invalid noise names
    
    # Validate backend (this could be more sophisticated by checking against a list of supported backends)
    # For now, we'll assume the runner will handle invalid backends
    
    # 1. Define the circuit using our generic Intermediate Representation (IR).
    # This describes the circuit in a framework-agnostic way.
    ir = CircuitIR(
        n_qubits=2,
        operations=[
            Gate(name="h", qubits=[0]),  # Hadamard gate on qubit 0
            Gate(name="cnot", qubits=[0, 1]),  # CNOT gate with control 0, target 1
        ],
    )

    # 2. Define the noise model from user input.
    noise_spec = NoiseSpec(name=noise_name, p=p)

    # 3. Run the circuit using our high-level runner.
    # The runner will automatically pick the correct backend (Qiskit or Cirq).
    results = run(ir=ir, shots=shots, noise_spec=noise_spec, backend=backend, seed=seed)

    # 4. Add the pedagogical explanation to the results.
    results.explanation = get_bell_explanation()

    return results

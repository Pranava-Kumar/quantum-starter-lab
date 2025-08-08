# src/quantum_starter_lab/explain.py
# Generates simple, pedagogical explanations for quantum demos.

def get_bell_explanation(noise_info: str = "") -> str:
    """Returns the explanation for the Bell state demo."""
    base_explanation = (
        "The Bell state is a famous example of quantum entanglement. "
        "The circuit uses a Hadamard gate to create superposition, and a CNOT gate "
        "to entangle two qubits. In an ideal run, you will only measure '00' or "
        "'11', each with 50% probability. Measuring one qubit instantly tells you "
        "the state of the other."
    )
    if noise_info:
        return f"{base_explanation} {noise_info}"
    return base_explanation

def get_dj_explanation(n_qubits: int, noise_info: str = "") -> str:
    """Returns the explanation for the Deutsch-Jozsa demo."""
    return (
        f"This is the Deutsch-Jozsa demo for {n_qubits} qubits. It determines if "
        f"a function is constant or balanced in one query."
    )

def get_bv_explanation(n_qubits: int, noise_info: str = "") -> str:
    """Returns the explanation for the Bernstein-Vazirani demo."""
    return (
        f"This is the Bernstein-Vazirani demo for {n_qubits} qubits. It finds a "
        f"secret string hidden in a function."
    )

def get_grover_explanation(n_qubits: int, noise_info: str = "") -> str:
    """Returns the explanation for the Grover's search demo."""
    return (
        f"This is Grover's search demo for {n_qubits} qubits. It finds a 'marked' "
        f"item in an unsorted database much faster than a classical computer."
    )

def get_teleportation_explanation(noise_info: str = "") -> str:
    """Returns the explanation for the quantum teleportation demo."""
    return (
        "Quantum teleportation allows one qubit to be sent to another via entanglement. "
        "In this demo, a qubit is teleported from Alice to Bob."
    )

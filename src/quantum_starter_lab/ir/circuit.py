# src/quantum_starter_lab/ir/circuit.py
# Defines the framework-agnostic data structures for a quantum circuit.

import dataclasses
from typing import Any, Dict, List, Optional

@dataclasses.dataclass(frozen=True)
class Gate:
    """
    A generic representation of a single quantum gate (an operation).
    """
    name: str  # e.g., 'h', 'cnot', 'mcz'
    qubits: List[int] # The qubit indices this gate acts on
    parameters: Optional[Dict[str, Any]] = None # For gates like U-gates or custom oracles
    classical_control_bit: Optional[int] = None # For classically controlled gates (teleportation)

@dataclasses.dataclass(frozen=True)
class CircuitIR:
    """
    An Intermediate Representation (IR) of a full quantum circuit.

    This is a framework-agnostic description that can be translated
    into a Qiskit circuit, a Cirq circuit, or any other backend.
    """
    n_qubits: int
    operations: List[Gate]
    measure_all_key: str = "m" # The key used for measurements in backends like Cirq

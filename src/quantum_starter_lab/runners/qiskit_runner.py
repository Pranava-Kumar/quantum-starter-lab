# src/quantum_starter_lab/runners/qiskit_runner.py
# The implementation of a quantum runner using IBM's Qiskit framework.

from typing import Optional
import qiskit
from qiskit_aer import Aer

from .base import QuantumRunner
from ..results import Results
from ..noise.spec import NoiseSpec
from ..noise.qiskit_noise import apply_qiskit_noise
from ..ir.circuit import CircuitIR
from ..utils.hist import normalize_counts


class QiskitRunner(QuantumRunner):
    """A runner that executes circuits using the Qiskit Aer simulator."""

    def run(
        self,
        ir: CircuitIR,
        shots: int,
        noise_spec: Optional[NoiseSpec] = None,
        seed: Optional[int] = None,
    ) -> Results:
        """
        Runs the given circuit IR on Qiskit's Aer simulator.
        """
        # 1. Translate our IR to a Qiskit QuantumCircuit
        qiskit_circuit = self._ir_to_qiskit_circuit(ir)

        # 2. Get the simulator backend
        simulator = Aer.get_backend("aer_simulator")

        # 3. Build the noise model if specified
        noise_model = None
        if noise_spec and noise_spec.name != "none":
            noise_model = apply_qiskit_noise(noise_spec)

        # 4. Run the simulation
        result = simulator.run(
            qiskit_circuit, shots=shots, seed_simulator=seed, noise_model=noise_model
        ).result()

        # 5. Process the results into our standard format
        counts = result.get_counts(qiskit_circuit)
        probabilities = normalize_counts(counts)

        # 6. Create and return our standard Results object
        return Results(
            counts=counts,
            probabilities=probabilities,
            circuit_diagram=qiskit_circuit.draw(output="text").single_string(),
            explanation="",  # The explanation is added at a higher level
            raw_backend_result=result,
        )

    def _ir_to_qiskit_circuit(self, ir: CircuitIR) -> qiskit.QuantumCircuit:
        """Translates our internal circuit representation to a Qiskit circuit."""
        circuit = qiskit.QuantumCircuit(ir.n_qubits)

        for op in ir.operations:
            # Map our gate names to Qiskit gate methods
            if op.name.lower() == "h":
                circuit.h(op.qubits)
            elif op.name.lower() == "x":
                circuit.x(op.qubits)
            elif op.name.lower() == "cnot":
                # THE FIX IS HERE: Changed from .cnot() to .cx()
                circuit.cx(op.qubits[0], op.qubits[1])
            # Add more gate mappings here (e.g., for Z, Y, etc.)

        # Add measurement at the end
        circuit.measure_all()
        return circuit

# src/quantum_starter_lab/runners/cirq_runner.py
# The implementation of a quantum runner using Google's Cirq framework.

from typing import Optional
import cirq

from .base import QuantumRunner
from ..results import Results
from ..noise.spec import NoiseSpec
from ..noise.cirq_noise import apply_cirq_noise
from ..ir.circuit import CircuitIR
from ..utils.hist import normalize_counts
from ..utils.bitstrings import pad_bitstrings


class CirqRunner(QuantumRunner):
    """A runner that executes circuits using the Cirq simulator."""

    def run(
        self,
        ir: CircuitIR,
        shots: int,
        noise_spec: Optional[NoiseSpec] = None,
        seed: Optional[int] = None,
    ) -> Results:
        """
        Runs the given circuit IR on Cirq's simulator.

        Args:
            ir: The intermediate representation of the circuit.
            shots: The number of simulation shots.
            noise_spec: The specification for the noise model.
            seed: A seed for the simulator's random number generator.

        Returns:
            A Results object with the simulation outcome.
        """
        # 1. Convert our IR to a Cirq circuit
        cirq_circuit = self._ir_to_cirq_circuit(ir)

        # 2. Add noise to the circuit if specified
        if noise_spec and noise_spec.name != "none":
            noisy_circuit = apply_cirq_noise(cirq_circuit, noise_spec)
            simulator = cirq.DensityMatrixSimulator(seed=seed)
            result = simulator.run(noisy_circuit, repetitions=shots)
        else:
            simulator = cirq.Simulator(seed=seed)
            result = simulator.run(cirq_circuit, repetitions=shots)

        # 3. Process the results into our standard format
        measurements = result.measurements.get(ir.measure_all_key, [])
        counts = self._process_cirq_measurements(measurements, ir.n_qubits)

        # 4. Pad bitstrings for consistency
        padded_counts = pad_bitstrings(counts, ir.n_qubits)

        # 5. Create and return our standard Results object
        probabilities = normalize_counts(padded_counts)

        return Results(
            counts=padded_counts,
            probabilities=probabilities,
            circuit_diagram=cirq_circuit.to_text_diagram(),
            explanation="",  # The explanation is added at a higher level
            raw_backend_result=result,
        )

    def _ir_to_cirq_circuit(self, ir: CircuitIR) -> cirq.Circuit:
        """Translates our internal circuit representation to a Cirq circuit."""
        qubits = cirq.LineQubit.range(ir.n_qubits)
        circuit = cirq.Circuit()

        for op in ir.operations:
            # Map our gate names to Cirq gate objects
            target_qubits = [qubits[i] for i in op.qubits]
            if op.name.lower() == "h":
                circuit.append(cirq.H.on_each(*target_qubits))
            elif op.name.lower() == "x":
                circuit.append(cirq.X.on_each(*target_qubits))
            elif op.name.lower() == "cnot":
                circuit.append(cirq.CNOT(target_qubits[0], target_qubits[1]))
            # Add more gate mappings here (e.g., for Z, Y, etc.)

        # Add measurement at the end
        circuit.append(cirq.measure(*qubits, key=ir.measure_all_key))
        return circuit

    def _process_cirq_measurements(self, measurements, n_qubits) -> dict:
        """Converts Cirq's measurement format into a counts dictionary."""
        counts = {}
        for measurement in measurements:
            # Convert array of [0, 1] to bitstring "01"
            bitstring = "".join(map(str, measurement))
            counts[bitstring] = counts.get(bitstring, 0) + 1
        return counts

# src/quantum_starter_lab/ir/ascii.py
# A simple function to draw a CircuitIR object as a text diagram.

from .circuit import CircuitIR

def draw_circuit_ascii(ir: CircuitIR) -> str:
    """
    Generates a simple, single-string ASCII art diagram of the circuit.
    
    This is a basic implementation for pedagogical purposes.
    """
    if not ir.operations:
        return "\n".join([f"q{i}: --" for i in range(ir.n_qubits)])

    # Initialize the drawing grid
    width = len(ir.operations) * 4 + 1
    diagram = [['-' for _ in range(width)] for _ in range(ir.n_qubits)]

    for op_idx, op in enumerate(ir.operations):
        pos = op_idx * 4 + 2
        
        if len(op.qubits) == 1:
            # Single-qubit gate
            q = op.qubits[0]
            diagram[q][pos] = f'[{op.name.upper()}]'
        elif op.name.lower() == 'cnot' and len(op.qubits) == 2:
            # CNOT gate
            control, target = op.qubits[0], op.qubits[1]
            diagram[control][pos] = '[X]'
            diagram[target][pos] = '[+]'
            # Draw the vertical line
            for q in range(min(control, target) + 1, max(control, target)):
                diagram[q][pos] = ' | '
        # Add more gate drawings here as needed...
    
    # Format the final output string
    output_lines = []
    for i in range(ir.n_qubits):
        line_str = "".join(str(item).center(3) for item in diagram[i])
        output_lines.append(f"q{i}: {line_str}")
        
    return "\n".join(output_lines)

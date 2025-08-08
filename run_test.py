from quantum_starter_lab.api import make_bell

print("--- Running quantum-starter-lab! ---")
results = make_bell(backend="qiskit.aer", seed=42)
print(results)
results.plot()
print("--- Demo complete! ---")

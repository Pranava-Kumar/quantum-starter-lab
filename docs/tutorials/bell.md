# Tutorial: The Bell State - Quantum "Hello, World!"

The Bell state is the simplest and most famous example of **quantum entanglement**. It's often called the "Hello, World!" of quantum computing because it's one of the first circuits newcomers learn.

## What is a Bell State?

Imagine you have two quantum bits (qubits). When you put them into a Bell state, they become linked in a special way.
-   Their fates are intertwined: if you measure one, you instantly know the state of the other, no matter how far apart they are.
-   In the simplest Bell state, if you measure one qubit and find it's a `0`, the other one will also be a `0`. If you find a `1`, the other will also be a `1`.
-   Before measurement, neither qubit has a definite state. They are in a **superposition** of being `00` and `11` at the same time.

The circuit to create it is very simple:
1.  A **Hadamard (H)** gate puts the first qubit into a superposition.
2.  A **Controlled-NOT (CNOT)** gate entangles the two qubits.

## Running the Demo

With `quantum-starter-lab`, you can create, run, and see the results of a Bell state with just one line of code.

from quantum_starter_lab.api import make_bell

Run the ideal, noiseless simulation
results = make_bell()

Print the simple explanation and see the counts
print(results)

Show the circuit diagram and histogram plot
results.plot()

## Interpreting the Ideal Results

In a perfect (ideal) simulation, you will only ever measure two outcomes:
-   `00`
-   `11`

Each of these should appear approximately 50% of the time. This 50/50 split proves that the qubits were in a perfect superposition before you measured them.

## Seeing the Effect of Noise

Real quantum computers are "noisy," which causes errors. Your package makes it easy to see this effect. Let's run the same demo with some **depolarizing noise**.

from quantum_starter_lab.api import make_bell

Run the simulation with a 5% chance of a depolarizing error
noisy_results = make_bell(noise_name="depolarizing", p=0.05)

print(noisy_results)

noisy_results.plot()

Now, you will see small counts for `01` and `10`. These are error states that shouldn't appear ideally. The `fidelity` score in the results tells you how close your noisy result was to the perfect one. A lower score means more noise!
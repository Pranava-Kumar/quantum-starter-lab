# Tutorial: Quantum Teleportation

Quantum teleportation is a real protocol that allows you to transmit the **exact state** of a quantum bit (qubit) from one location to another, without physically sending the particle itself.

**Important**: This is not like Star Trek! We are not teleporting matter, only **quantum information**.

## The Key Ingredients

To make teleportation work, you need two things:
1.  **A Shared Entangled Pair**: The sender (Alice) and the receiver (Bob) must each hold one qubit from a pre-shared, entangled Bell pair. This is the "quantum channel" that links them.
2.  **A Classical Channel**: Alice needs to send two regular classical bits of information to Bob (e.g., over the phone or internet).

## The Protocol: A Simple Walkthrough

Let's say Alice wants to teleport the state of her "message" qubit to Bob.
1.  **Alice's Part**: Alice performs a set of operations on her message qubit and her half of the entangled pair. She then measures her two qubits, and the result she gets is two classical bits (e.g., `10`).
2.  **Classical Communication**: Alice sends these two bits to Bob.
3.  **Bob's Part**: Based on the two bits he receives from Alice, Bob performs a specific correction on his half of the entangled pair.

After Bob applies the correction, his qubit will be in the **exact same state** as Alice's original message qubit. The original message state at Alice's end is destroyed in the process due to the No-Cloning Theorem.

## Running the Teleportation Demo

The `quantum-starter-lab` package lets you simulate this entire protocol with one function.

from quantum_starter_lab.api import teleportation

Run the teleportation demo
By default, it teleports a simple state.
results = teleportation()

print(results)
results.plot()

## Interpreting the Results

The circuit has three qubits:
-   `q0`: Alice's message qubit.
-   `q1`: Alice's half of the entangled pair.
-   `q2`: Bob's half of the entangled pair.

The state of `q0` is teleported to `q2`. When you look at the measurement results, you should focus on the state of the third qubit (`q2`, the rightmost bit). In an ideal simulation, its state will perfectly match the initial state that was prepared on `q0`.
# Tutorial: Grover's Search - Finding a Needle in a Haystack

Grover's algorithm is one of the most famous quantum algorithms. It provides a significant speedup for searching an **unsorted database**.

## The Problem: Unstructured Search

Imagine you have a giant, unsorted phone book with N entries, and you're looking for one specific name (the "marked item"). Classically, you have no choice but to check the entries one by one. On average, you'd have to check N/2 entries, and in the worst case, all N of them.

**The Quantum Solution**: Grover's algorithm can find the marked item in approximately **√N** (square root of N) steps. This is a **quadratic speedup**, which is massive for large databases.

## How it Works: Amplitude Amplification

Grover's algorithm doesn't "search" in the classical sense. Instead, it uses a clever trick called **amplitude amplification**:
1.  It starts by putting all possible items into an equal superposition. Every item has the same small probability of being measured.
2.  It then uses two main components in a loop:
    *   An **Oracle** that "marks" the correct item by flipping its phase (making it negative). This doesn't change the probability, so you can't measure it yet.
    *   A **Diffuser** that flips all the states around their average amplitude. This clever move dramatically *increases* the amplitude of the marked item and *decreases* the amplitude of all others.
3.  After the right number of loops, the probability of measuring the marked item becomes very high.

## Running the Grover's Demo

Let's search for the state `101` in a 3-qubit search space (which has 2³ = 8 items).

from quantum_starter_lab.api import grover

Search for the marked item "101"
results = grover(n_qubits=3, marked_item="101")

print(results)
results.plot()

## Interpreting the Results

If you look at the histogram from the results, you will see that the `101` state has a much, much higher probability of being measured than any other state. In an ideal run, this probability is close to 100%.

Grover's algorithm is a powerful tool and a key building block for many other quantum algorithms.
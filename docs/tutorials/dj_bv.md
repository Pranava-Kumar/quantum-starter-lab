# Tutorial: Deutsch-Jozsa and Bernstein-Vazirani

These two algorithms are famous early examples that show how a quantum computer can solve a specific problem much faster than a classical computer by using **quantum parallelism**.

## The Deutsch-Jozsa (DJ) Problem: Constant or Balanced?

Imagine a "black box" function (an oracle) that takes a binary string (like `011`) and returns either `0` or `1`. You are promised that the function is one of two types:
-   **Constant**: It always returns the same value (all `0`s or all `1`s) for every input.
-   **Balanced**: It returns `0` for exactly half of the inputs and `1` for the other half.

**The Challenge**: How many times do you have to check the function to know if it's constant or balanced? Classically, in the worst case, you might have to check over half the inputs.

**The Quantum Solution**: The DJ algorithm figures it out in **just one shot**!

### Running the DJ Demo

from quantum_starter_lab.api import deutsch_jozsa

Run the demo for a 3-qubit balanced function
results = deutsch_jozsa(n_qubits=3, oracle_type="balanced")

print(results)
results.plot()

### Interpreting the Results
-   If you measure the all-zeros state (`000` in this case), the function was **constant**.
-   If you measure *any other state*, the function was **balanced**.

## The Bernstein-Vazirani (BV) Problem: Find the Secret String

Imagine an oracle that hides a secret binary string, let's call it `s`. The oracle takes your input string `x` and returns the bitwise dot product of `x` and `s` (modulo 2).

**The Challenge**: Classically, to find an n-bit secret string `s`, you have to call the function `n` times, feeding it inputs like `100...`, `010...`, etc., to find each bit of `s` one by one.

**The Quantum Solution**: The BV algorithm finds the entire secret string in **just one shot**!

### Running the BV Demo

from quantum_starter_lab.api import bernstein_vazirani

Find the 4-bit secret string "1011"
secret = "1011"
results = bernstein_vazirani(n_qubits=4, secret_string=secret)

print(results)
results.plot()

### Interpreting the Results
In an ideal, noiseless run, the measurement result you get will be **exactly the secret string**! This is a stunning demonstration of quantum parallelism, where the algorithm effectively "tests" all possibilities at once.
# Prompt: Generate a New Framework Adapter

Your task is to create a new quantum runner and noise adapter for the **[FRAMEWORK_NAME]** framework (e.g., "PennyLane", "Amazon Braket").

Follow these steps precisely:

## 1. Create the Runner File

Create a new file at `src/quantum_starter_lab/runners/[FRAMEWORK_NAME]_runner.py`.

Inside this file, create a class named `[FRAMEWORK_NAME]Runner` that inherits from `QuantumRunner` in `src/quantum_starter_lab/runners/base.py`.

Implement the `run` method with the exact signature from the base class.

## 2. Implement the IR-to-Framework Translator

Inside the `[FRAMEWORK_NAME]Runner` class, write a private helper method `_ir_to_[FRAMEWORK_NAME]_circuit` that takes our `CircuitIR` object and translates it into a native `[FRAMEWORK_NAME]` circuit object.

You must map the following gates from our IR:
-   `'h'` -> `[FRAMEWORK_NAME]`'s Hadamard gate
-   `'x'` -> `[FRAMEWORK_NAME]`'s X gate
-   `'cnot'` -> `[FRAMEWORK_NAME]`'s CNOT gate
-   `'mcz'` -> `[FRAMEWORK_NAME]`'s multi-controlled Z gate (if available, otherwise note the limitation).
-   `'u'` -> `[FRAMEWORK_NAME]`'s generic U gate.
-   Handle gates with `classical_control_bit` if the framework supports it.

## 3. Implement the Noise Translator

Create a new file at `src/quantum_starter_lab/noise/[FRAMEWORK_NAME]_noise.py`.

Inside this file, create a function `apply_[FRAMEWORK_NAME]_noise` that takes a `NoiseSpec` object and a native `[FRAMEWORK_NAME]` circuit. It should apply the corresponding noise channels from the framework's library.
-   `"bit_flip"` -> `[FRAMEWORK_NAME]`'s bit-flip channel
-   `"depolarizing"` -> `[FRAMEWORK_NAME]`'s depolarizing channel
-   If a noise type is not supported, log a warning and return the circuit unchanged.

## 4. Implement Result Processing

Back in your runner's `run` method, after executing the circuit, process the native results from `[FRAMEWORK_NAME]` back into our standard `Results` object from `src/quantum_starter_lab/results.py`.
-   Ensure the `counts` dictionary is correctly formatted.
-   Use the `normalize_counts` utility to get probabilities.
-   Generate a `circuit_diagram` string using the framework's native drawing tool.

## 5. Register the New Runner

In `src/quantum_starter_lab/runners/__init__.py`, add the new runner to the `RUNNER_MAP` dictionary. The key should be a descriptive string like `"[FRAMEWORK_NAME].default"`.

## 6. Write a Basic Test

Create a new test file at `tests/test_[FRAMEWORK_NAME]_adapter.py`.

Write a simple test function `test_bell_state_on_[FRAMEWORK_NAME]` that:
1.  Calls `make_bell` with `backend="[FRAMEWORK_NAME].default"`.
2.  Asserts that the returned `Results` object is not None.
3.  Asserts that the measured counts contain only `'00'` and `'11'` (for a noiseless run).
4.  Asserts that the probabilities for `'00'` and `'11'` are both close to 0.5.

---
**Context Files to Provide to the AI:**
- `src/quantum_starter_lab/runners/base.py`
- `src/quantum_starter_lab/runners/qiskit_runner.py` (as an example)
- `src/quantum_starter_lab/ir/circuit.py`
- `src/quantum_starter_lab/noise/spec.py`

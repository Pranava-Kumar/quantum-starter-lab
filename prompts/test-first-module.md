# Prompt: Create a New Module Using Test-First Development

Your task is to create a new, fully tested module for the `quantum-starter-lab` package. You must follow the Test-First Development (TDD) workflow precisely.

The new feature to implement is: **[BRIEFLY DESCRIBE THE NEW FEATURE HERE]**

## Workflow Steps:

**Step 1: Write the Tests First (`pytest`)**

Before writing any implementation code, create the test file.

-   **File Path**: `tests/[TEST_FILE_NAME].py`
-   **Content**: Write a suite of `pytest` functions that define the expected behavior of the new module.
-   **Test Coverage**: You must include tests for:
    -   The "happy path" (correct inputs leading to expected outputs).
    -   Edge cases (e.g., empty inputs, zero values, single-qubit cases).
    -   Expected errors (e.g., what should happen if the user provides invalid input). Use `pytest.raises` for this.
    -   Reproducibility (if randomness is involved, test that providing a `seed` gives the same result every time).

**Step 2: Write the Source Code to Pass the Tests**

After defining the tests, write the source code for the new module.

-   **File Path**: `src/quantum_starter_lab/[MODULE_PATH]/[SOURCE_FILE_NAME].py`
-   **Content**: Implement the functions and classes required to make all the tests you wrote in Step 1 pass.
-   **Code Quality**:
    -   The code must be fully type-hinted.
    -   Every public function and class must have a clear, user-friendly docstring explaining what it does, its arguments, and what it returns.

## Final Output Structure

Please provide your response in two clearly labeled code blocks:

**1. The Test File**
tests/[TEST_FILE_NAME].py
PASTE THE COMPLETE TEST CODE HERE

**2. The Source Code File**
src/quantum_starter_lab/[MODULE_PATH]/[SOURCE_FILE_NAME].py
PASTE THE COMPLETE SOURCE CODE HERE

---
**Context to Provide to the AI:**
- A clear description of the new feature.
- The desired file paths for the test and source files.
- Any related source code files that the new module will interact with.
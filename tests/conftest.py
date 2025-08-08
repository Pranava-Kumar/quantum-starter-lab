# tests/conftest.py
# This file contains shared fixtures for pytest.

import pytest

# A list of all backends that the package supports.
# Any test that uses the 'backend' fixture will be run for each of these values.
SUPPORTED_BACKENDS = ["qiskit.aer", "cirq.simulator"]

@pytest.fixture(params=SUPPORTED_BACKENDS)
def backend(request):
    """A fixture that provides each supported backend name."""
    return request.param

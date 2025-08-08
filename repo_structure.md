quantum-starter-lab/
├─ pyproject.toml
├─ README.md
├─ LICENSE
├─ CODE_OF_CONDUCT.md
├─ CONTRIBUTING.md
├─ SECURITY.md
├─ CITATION.cff
├─ .gitignore
├─ .pre-commit-config.yaml
├─ Makefile
├─ constraints/
│ ├─ requirements-qiskit.txt
│ └─ requirements-cirq.txt
├─ src/
│ └─ quantum_starter_lab/
│ ├─ init.py
│ ├─ api.py
│ ├─ results.py
│ ├─ explain.py
│ ├─ plotting.py
│ ├─ cli.py
│ ├─ utils/
│ │ ├─ init.py
│ │ ├─ bitstrings.py
│ │ ├─ rng.py
│ │ └─ hist.py
│ ├─ noise/
│ │ ├─ init.py
│ │ ├─ spec.py
│ │ ├─ qiskit_noise.py
│ │ └─ cirq_noise.py
│ ├─ runners/
│ │ ├─ init.py
│ │ ├─ base.py
│ │ ├─ qiskit_runner.py
│ │ └─ cirq_runner.py
│ ├─ ir/
│ │ ├─ init.py
│ │ ├─ circuit.py
│ │ └─ ascii.py
│ └─ demos/
│ ├─ bell.py
│ ├─ dj.py
│ ├─ bv.py
│ ├─ grover.py
│ └─ teleportation.py
├─ tests/
│ ├─ conftest.py
│ ├─ test_bell.py
│ ├─ test_dj_bv_grover.py
│ ├─ test_noise.py
│ ├─ test_plotting.py
│ └─ test_endianness.py
├─ docs/
│ ├─ mkdocs.yml
│ ├─ index.md
│ ├─ quickstart.md
│ ├─ api.md
│ └─ tutorials/
│ ├─ bell.md
│ ├─ dj_bv.md
│ └─ grover.md
├─ examples/
│ ├─ bell_notebook.ipynb
│ └─ dj_vs_balanced.ipynb
├─ .github/
│ └─ workflows/
│ ├─ ci.yml
│ └─ release.yml
└─ prompts/
├─ tests-first-module.md
├─ adapter-generator.md
├─ debug-failing-test.md
├─ perf-profile-optimize.md
└─ doc-notebook-generator.md
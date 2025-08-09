Contributing to quantum-starter-lab

Thank you for your interest in contributing to quantum-starter-lab! This project aims to make quantum computing accessible for education, research, and experimentation. Whether you're fixing bugs, adding new features, improving documentation, or suggesting ideas, your contributions are welcome and valued.

By contributing, you help build a better tool for the quantum community. Please follow these guidelines to ensure a smooth process.

Code of Conduct

This project adheres to the Contributor Covenant Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to pranavakumar.it@gmail.com.

How to Contribute
There are many ways to contribute:

Report Issues: If you find a bug, have a feature request, or spot documentation issues, open an issue on GitHub. Provide as much detail as possible, including steps to reproduce, expected behavior, and screenshots if applicable.

Suggest Improvements: For enhancements like new algorithms (e.g., VQE, QAOA) or backend integrations, open an issue first to discuss before coding.

Submit Pull Requests: For code changes, follow the steps below.

Setting Up for Development
To contribute code, set up a local development environment:

Fork the Repository:

Go to https://github.com/Pranava-Kumar/quantum-starter-lab.

Click "Fork" to create your own copy.

Clone Your Fork:

git clone https://github.com/YOUR-USERNAME/quantum-starter-lab.git
cd quantum-starter-lab
Create a Virtual Environment (using uv for speed):

uv venv
.venv\Scripts\activate  # On Windows; use source .venv/bin/activate on Unix
Install Dependencies:

uv sync --all-extras --dev
uv pip install -e .  # Editable install for development
Verify Setup:

make lint  # Check code style
make test  # Run all tests
Requirements: Python >=3.10. If tests fail, check for missing dependencies like Qiskit or Cirq.

Development Guidelines
Branching: Create a new branch for your work: git checkout -b feature/your-feature-name or bugfix/issue-number.

Coding Style: Follow PEP 8. Use Ruff for linting (make lint). Keep code modular and well-commented.

Commits: Write clear, concise commit messages (e.g., "Add VQE function with scipy optimizer").

Testing: Add unit tests for new features in the tests/ folder. Aim for 100% coverage. Run make test before submitting.

Documentation: Update README.md or add to docs/ if introducing new features. Use Markdown for clarity.

Pull Request Process:

Push your branch: git push origin your-branch-name.

Open a Pull Request on the original repo.

Reference any related issues (e.g., "Fixes #123").

Describe changes, why they're needed, and how to test them.

Your PR will be reviewed; be open to feedback.

Areas for Contribution
Bug Fixes: Address test failures or runtime errors.

New Demos: Add advanced algorithms like VQE or QAOA.

Enhancements: Improve noise models, add real hardware support, or integrate ML tools.

Docs and Examples: Write tutorials or Jupyter notebooks.

Performance: Optimize simulations for larger qubit counts.

First-time contributors: Look for issues labeled "good first issue" or "help wanted".

License
By contributing, you agree that your contributions will be licensed under the project's Apache License 2.0.

Thank you for helping make quantum-starter-lab better! If you have questions, open an issue or email pranavakumar.it@gmail.com.
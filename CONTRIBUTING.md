# Contributing to quantum-starter-lab

First off, thank you for considering contributing! We are thrilled you're here and excited to collaborate with you. Your contributions, no matter how small, are valued and help make this project better for everyone [1].

This document provides a set of guidelines for contributing to `quantum-starter-lab`.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](./CODE_OF_CONDUCT.md). Please read it to understand the standards of behavior we expect [4].

## How Can I Contribute?

There are many ways to contribute, from writing code and documentation to reporting bugs and suggesting new features.

### Reporting Bugs

If you find a bug, please open a new **issue** on our GitHub repository. A great bug report includes:
-   A clear and descriptive title.
-   A description of the steps to reproduce the bug.
-   What you expected to happen vs. what actually happened.
-   The version of `quantum-starter-lab` and Python you are using.

### Suggesting Enhancements

If you have an idea for a new feature or an improvement, please open an **issue** to discuss it first. This allows us to coordinate efforts and ensure the feature aligns with the project's goals before you spend time on implementation [6].

### Your First Code Contribution

Ready to write some code? Here’s how to set up your environment and submit your changes.

#### 1. Fork and Clone the Repository

First, **fork** the repository to your own GitHub account. Then, clone your fork to your local machine [5]:

git clone https://github.com/Pranava-Kumar/quantum-starter-lab.git
cd quantum-starter-lab

#### 2. Set Up Your Development Environment

We use `uv` for package management. To install all the dependencies needed for development (including tools for testing and linting), run:
uv sync --all-extras --dev

Or, you can use the `make` shortcut:
make install

#### 3. Create a New Branch

Create a descriptive branch for your changes [5]:
git checkout -b feature/my-cool-new-feature

#### 4. Make Your Changes and Run Checks

Write your code! As you work, please adhere to the following:
-   **Coding Style**: We use `black` for code formatting and `ruff` for linting. You can automatically format your code by running `make format`.
-   **Testing**: If you add a new feature, please add tests for it. You can run the full test suite with `make test`. All tests must pass for your contribution to be accepted [6, 10].

#### 5. Commit and Push

Commit your changes with a clear commit message:
git commit -m "feat: Add my cool new feature"
git push origin feature/my-cool-new-feature

#### 6. Submit a Pull Request

Finally, go to your fork on GitHub and open a **Pull Request (PR)** to the `main` branch of the original repository. Provide a clear description of your changes in the PR.

Once you submit your PR, a project maintainer will review it. We appreciate your patience and will do our best to provide feedback in a timely manner.

Thank you again for your contribution!
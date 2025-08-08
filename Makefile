# Makefile for quantum-starter-lab - Common development commands

# This tells 'make' that these are command aliases, not files.
.PHONY: help install test lint format docs clean

help:
	@echo "Available commands:"
	@echo "  make install    - Install all dependencies for development"
	@echo "  make test       - Run the pytest test suite"
	@echo "  make lint       - Check code for style errors with ruff"
	@echo "  make format     - Automatically format code with ruff and black"
	@echo "  make docs       - Serve the documentation website locally"
	@echo "  make clean      - Remove temporary build files and caches"

install:
	uv sync --all-extras --dev

test:
	uv run pytest -v

lint:
	uv run ruff check .

format:
	uv run ruff format .
	uv run black .

docs:
	uv run mkdocs serve

clean:
	rm -rf .pytest_cache .coverage htmlcov dist/ build/
	find . -type d -name "__pycache__" -exec rm -rf {} +

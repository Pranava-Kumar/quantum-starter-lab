# src/quantum_starter_lab/cli.py
# Simple CLI for running quantum demos from the terminal.

import argparse
from .demos import (
    bell,
    dj,
    bv,
    grover,
    teleportation,
)  # Import demo functions (add these later)


def main():
    parser = argparse.ArgumentParser(
        description="quantum-starter-lab CLI: Run beginner quantum demos easily."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available demos")

    # Bell demo command
    bell_parser = subparsers.add_parser("bell", help="Run Bell state demo")
    bell_parser.add_argument(
        "--noise",
        default="none",
        choices=["none", "bit_flip", "depolarizing"],
        help="Noise type",
    )
    bell_parser.add_argument(
        "--p", type=float, default=0.0, help="Noise probability (0.0 to 1.0)"
    )
    bell_parser.add_argument(
        "--shots", type=int, default=1024, help="Number of simulation shots"
    )
    bell_parser.add_argument(
        "--seed", type=int, default=42, help="Random seed for reproducibility"
    )
    bell_parser.add_argument("--backend", default="qiskit.aer", help="Backend to use")
    bell_parser.add_argument(
        "--plot", action="store_true", help="Show plot (requires matplotlib)"
    )

    # Deutsch-Jozsa demo command (add similar for others)
    dj_parser = subparsers.add_parser("dj", help="Run Deutsch-Jozsa demo")
    dj_parser.add_argument("n", type=int, help="Number of qubits")
    # Add more args like above...

    # Add parsers for bv, grover, teleportation similarly
    # bv_parser = subparsers.add_parser("bv", help="Run Bernstein-Vazirani demo")
    # ... (copy pattern from bell)

    args = parser.parse_args()

    if args.command == "bell":
        results = bell.make_bell(
            noise=args.noise,
            p=args.p,
            shots=args.shots,
            seed=args.seed,
            backend=args.backend,
        )
        print(results.explanation)  # Print the plain-language summary
        print(f"Counts: {results.counts}")
        if args.plot:
            results.plot()  # This will show the plot if matplotlib is installed
    elif args.command == "dj":
        # Similar: results = dj.deutsch_jozsa(args.n, ...)
        pass  # Implement later
    # Add elif for other commands
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

# src/quantum_starter_lab/cli.py
# Simple CLI for running quantum demos from the terminal.

import argparse

from .demos import (
    bell,
    dj,
    bv,
    grover,
    teleportation,
    qft,
)  # Import demo functions


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

    # Deutsch-Jozsa demo command
    dj_parser = subparsers.add_parser("dj", help="Run Deutsch-Jozsa demo")
    dj_parser.add_argument("n", type=int, help="Number of qubits")
    dj_parser.add_argument(
        "--oracle-type",
        default="constant",
        choices=["constant", "balanced"],
        help="Type of oracle",
    )
    dj_parser.add_argument(
        "--shots", type=int, default=1024, help="Number of simulation shots"
    )
    dj_parser.add_argument(
        "--seed", type=int, default=42, help="Random seed for reproducibility"
    )
    dj_parser.add_argument("--backend", default="qiskit.aer", help="Backend to use")
    dj_parser.add_argument(
        "--plot", action="store_true", help="Show plot (requires matplotlib)"
    )

    # Bernstein-Vazirani demo command
    bv_parser = subparsers.add_parser("bv", help="Run Bernstein-Vazirani demo")
    bv_parser.add_argument("n", type=int, help="Number of qubits")
    bv_parser.add_argument("secret", type=str, help="Secret string")
    bv_parser.add_argument(
        "--shots", type=int, default=1024, help="Number of simulation shots"
    )
    bv_parser.add_argument(
        "--seed", type=int, default=42, help="Random seed for reproducibility"
    )
    bv_parser.add_argument("--backend", default="qiskit.aer", help="Backend to use")
    bv_parser.add_argument(
        "--plot", action="store_true", help="Show plot (requires matplotlib)"
    )

    # Grover's search demo command
    grover_parser = subparsers.add_parser("grover", help="Run Grover's search demo")
    grover_parser.add_argument("n", type=int, help="Number of qubits")
    grover_parser.add_argument("marked", type=str, help="Marked item")
    grover_parser.add_argument(
        "--shots", type=int, default=1024, help="Number of simulation shots"
    )
    grover_parser.add_argument(
        "--seed", type=int, default=42, help="Random seed for reproducibility"
    )
    grover_parser.add_argument("--backend", default="qiskit.aer", help="Backend to use")
    grover_parser.add_argument(
        "--plot", action="store_true", help="Show plot (requires matplotlib)"
    )

    # Quantum teleportation demo command
    teleportation_parser = subparsers.add_parser(
        "teleportation", help="Run quantum teleportation demo"
    )
    teleportation_parser.add_argument(
        "--angle",
        type=float,
        default=0.0,
        help="Angle of the initial state (in radians)",
    )
    teleportation_parser.add_argument(
        "--shots", type=int, default=1024, help="Number of simulation shots"
    )
    teleportation_parser.add_argument(
        "--seed", type=int, default=42, help="Random seed for reproducibility"
    )
    teleportation_parser.add_argument(
        "--backend", default="qiskit.aer", help="Backend to use"
    )
    teleportation_parser.add_argument(
        "--plot", action="store_true", help="Show plot (requires matplotlib)"
    )

    # Quantum Fourier Transform demo command
    qft_parser = subparsers.add_parser("qft", help="Run Quantum Fourier Transform demo")
    qft_parser.add_argument("n", type=int, help="Number of qubits")
    qft_parser.add_argument(
        "--include-swaps",
        action="store_true",
        help="Include swaps to reverse qubit order",
    )
    qft_parser.add_argument(
        "--shots", type=int, default=1024, help="Number of simulation shots"
    )
    qft_parser.add_argument(
        "--noise",
        default="none",
        choices=["none", "bit_flip", "depolarizing"],
        help="Noise type",
    )
    qft_parser.add_argument(
        "--p", type=float, default=0.0, help="Noise probability (0.0 to 1.0)"
    )
    qft_parser.add_argument(
        "--seed", type=int, default=42, help="Random seed for reproducibility"
    )
    qft_parser.add_argument("--backend", default="qiskit.aer", help="Backend to use")
    qft_parser.add_argument(
        "--plot", action="store_true", help="Show plot (requires matplotlib)"
    )

    args = parser.parse_args()

    if args.command == "bell":
        results = bell.make_bell(
            noise_name=args.noise,
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
        results = dj.deutsch_jozsa(
            n_qubits=args.n,
            oracle_type=args.oracle_type,
            shots=args.shots,
            seed=args.seed,
            backend=args.backend,
        )
        print(results.explanation)
        print(f"Counts: {results.counts}")
        if args.plot:
            results.plot()
    elif args.command == "bv":
        results = bv.bernstein_vazirani(
            n_qubits=args.n,
            secret_string=args.secret,
            shots=args.shots,
            seed=args.seed,
            backend=args.backend,
        )
        print(results.explanation)
        print(f"Counts: {results.counts}")
        if args.plot:
            results.plot()
    elif args.command == "grover":
        results = grover.grover(
            n_qubits=args.n,
            marked_item=args.marked,
            shots=args.shots,
            seed=args.seed,
            backend=args.backend,
        )
        print(results.explanation)
        print(f"Counts: {results.counts}")
        if args.plot:
            results.plot()
    elif args.command == "teleportation":
        results = teleportation.teleportation(
            initial_state_angle=args.angle,
            shots=args.shots,
            seed=args.seed,
            backend=args.backend,
        )
        print(results.explanation)
        print(f"Counts: {results.counts}")
        if args.plot:
            results.plot()
    elif args.command == "qft":
        results = qft.make_qft(
            n_qubits=args.n,
            include_swaps=args.include_swaps,
            shots=args.shots,
            noise_name=args.noise,
            p=args.p,
            seed=args.seed,
            backend=args.backend,
        )
        print(results.explanation)
        print(f"Counts: {results.counts}")
        if args.plot:
            results.plot()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

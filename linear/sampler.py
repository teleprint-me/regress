"""
Copyright (C) 2024 Austin Berrio

Module: linear.sampler

Generalized sampler function that maps a domain to a codomain of integers with
flexible parameters for range and transformation.
"""

from argparse import ArgumentParser, Namespace
from random import randrange, seed


# Generate and print samples
def sample_space(start: int, stop: int) -> int:
    return list(range(start, stop))[randrange(stop - start)]


def get_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "-s",
        "--seed",
        type=int,
        default=42,
        help="Seed for deterministic output. Defaults to 42.",
    )
    parser.add_argument(
        "-d",
        "--deterministic",
        action="store_true",
        help="Enable deterministic output.",
    )
    parser.add_argument(
        "-n",
        "--size",
        type=int,
        default=10,
        help="Number of samples.",
    )
    parser.add_argument(
        "--start",
        type=int,
        default=1,
        help="Lower boundary of the sampled sequence.",
    )
    parser.add_argument(
        "--stop",
        type=int,
        default=6,
        help="Upper boundary of the sampled sequence.",
    )
    return parser.parse_args()


def main():
    # Get CLI arguments
    args = get_args()

    # Set the seed for deterministic output if the flag is provided
    if args.deterministic:
        seed(args.seed)

    samples = [sample_space(args.start, args.stop) for _ in range(args.size)]
    print(f"Sampled space: {samples}")


if __name__ == "__main__":
    main()

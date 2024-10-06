"""
Copyright (C) 2024 Austin Berrio

Module: linear.sampler

Generalized sampler function that maps a domain to a codomain of integers with
flexible parameters for range and transformation.
"""

from argparse import ArgumentParser, Namespace
from random import randrange, seed


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
        help="Enable deterministic output. Defaults to False.",
    )
    parser.add_argument(
        "-n",
        "--size",
        type=int,
        default=10,
        help="Number of samples. Defaults to 10.",
    )
    parser.add_argument(
        "--start",
        type=int,
        default=1,
        help="Lower boundary of the sampled sequence (inclusive). Defaults to 1.",
    )
    parser.add_argument(
        "--stop",
        type=int,
        default=7,
        help="Upper boundary of the sampled sequence (exclusive). Defaults to 7.",
    )
    return parser.parse_args()


def main():
    # Get user parameters
    args = get_args()

    # Population: Die faces, deck of cards, color wheel, etc.
    population = list(range(args.start, args.stop))
    population_size = len(population)

    # Total permutations with replacement: j^n
    total_permutations = int(pow(population_size, args.size))
    print(f"Total possible permutations with replacement: {total_permutations}")

    # Set a seed for deterministic output if the flag is set
    if args.deterministic:
        seed(args.seed)

    # Sample selected population
    for i in range(args.size):
        sample = population[randrange(len(population))]
        print(f"i: {i + 1}, sample: {sample}")


if __name__ == "__main__":
    main()

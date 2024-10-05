"""
Script: linear.roll

Generate a set of values for generating linear sequences with replacement

Generate a distribution set within a given range
"""

from argparse import ArgumentParser, Namespace
from math import pow
from random import randrange, seed


def dice_roll() -> int:
    return [1, 2, 3, 4, 5, 6][randrange(6)]


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
        "--sample-size",
        type=int,
        default=10,
        help="Number of dice rolls (sample size).",
    )
    return parser.parse_args()


def main():
    # Get user parameters
    args = get_args()

    # Population: Die faces
    population = [1, 2, 3, 4, 5, 6]
    population_size = len(population)

    # Total permutations with replacement: j^n
    total_permutations = int(pow(population_size, args.sample_size))
    print(f"Total possible permutations with replacement: {total_permutations}")

    # Set a seed for deterministic output if the flag is set
    if args.deterministic:
        seed(args.seed)

    # Sample rolls
    for i in range(args.sample_size):
        roll = dice_roll()
        print(f"i: {i + 1}, roll: {roll}")


if __name__ == "__main__":
    main()

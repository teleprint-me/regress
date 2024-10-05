"""
Script: linear.roll

Generate a set of values for generating linear sequences

Generate a distribution set within a given range
"""

from argparse import ArgumentParser, Namespace
from random import randrange, seed


def dice_roll() -> int:
    return [1, 2, 3, 4, 5, 6][randrange(1, 6)]


def get_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "-s",
        "--seed",
        type=int,
        default=42,
        help="See Douglas Adams. Defaults to 42.",
    )
    parser.add_argument(
        "-d",
        "--deterministic",
        action="store_true",
        help="Enable deterministic output. Default is False.",
    )
    return parser.parse_args()


def main():
    # Get user parameters
    args = get_args()
    # Set a seed for deterministic output if the flag is set
    if args.deterministic:
        seed(args.seed)
    # Create a sample size of 10
    for i in range(10):
        print(f"i: {i}, roll: {dice_roll()}")


if __name__ == "__main__":
    main()

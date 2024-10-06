"""
Copyright (C) 2024 Austin Berrio

Module: linear.sampler

Generalized sampler for replaceable selection sampling.
"""

import argparse
import random
from typing import Generator


class Sampler:
    def __init__(self, start: int, stop: int, size: int, seed: int):
        self.start = start
        self.stop = stop
        self.size = size
        self.seed = seed

    @property
    def population(self) -> int:
        return list(range(self.start, self.stop))

    @property
    def population_size(self) -> int:
        return len(self.population)

    @property
    def permutations(self) -> int:
        return int(pow(self.population_size, self.size))

    def sample(self) -> int:
        return self.population[random.randrange(self.population_size)]

    def generate(self) -> Generator:
        for i in range(self.size):
            yield self.sample()


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
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

    sampler = Sampler(args.start, args.stop, args.size, args.seed)
    print(f"Total possible permutations with replacement: {sampler.permutations}")

    # Set a seed for deterministic output if the flag is set
    if args.deterministic:
        random.seed(args.seed)

    # Sample selected population
    for i, sample in enumerate(sampler.generate()):
        print(f"i: {i + 1}, sample: {sample}")


if __name__ == "__main__":
    main()

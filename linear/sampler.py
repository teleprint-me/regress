"""
Copyright (C) 2024 Austin Berrio

Module: linear.sampler

Generalized sampler for replaceable selection sampling.
"""

import argparse
import dataclasses
import math
import random
from typing import Dict, Generator, Optional, Union


class ReplacementSampler:
    def __init__(self, range_start: int, range_stop: int, sample_size: int):
        self.range_start = range_start
        self.range_stop = range_stop
        self.sample_size = sample_size
        self.population = self.populate()

    @property
    def population_size(self) -> int:
        return len(self.population)

    @property
    def permutations(self) -> int:
        """
        The formula for the number of permutations with replacement is j^n,
        where j is the population size and n is the sample size.
        """
        return int(pow(self.population_size, self.sample_size))

    def populate(self) -> list[int]:
        """Generate elements based on the range."""
        return list(range(self.range_start, self.range_stop))

    def sample(self) -> int:
        return self.population[random.randrange(self.population_size)]

    def generate(self) -> Generator:
        for _ in range(self.sample_size):
            yield self.sample()


class NonReplacementSampler(ReplacementSampler):
    @property
    def permutations(self) -> int:
        """
        The formula for permutations is (j! / (j - n)!), where j is the
        population size and n is the sample size.
        """
        # Ensure the population is large enough for the requested sample size
        if self.sample_size > self.population_size:
            return 0
        return math.factorial(self.population_size) // math.factorial(
            self.population_size - self.sample_size
        )

    def sample(self) -> int:
        if not self.population:
            raise StopIteration("No more elements to sample.")
        return self.population.pop(random.randrange(len(self.population)))

    def generate(self) -> Generator[int, None, None]:
        for _ in range(min(self.sample_size, self.population_size)):
            yield self.sample()


def get_sampler(
    args: argparse.Namespace,
) -> Union[ReplacementSampler, NonReplacementSampler]:
    sampler = None
    if args.non_replacement:
        sampler = NonReplacementSampler
    else:
        sampler = ReplacementSampler
    return sampler(args.start, args.stop, args.size)


def get_sampled_frequency(
    sampler: Union[ReplacementSampler, NonReplacementSampler]
) -> Dict[int, int]:
    # Collect sampled frequency metadata
    frequency = {}
    for sample in sampler.generate():
        element = frequency.get(sample, 0)
        frequency[sample] = element + 1
    return frequency


def print_sampled_frequency(
    frequency: Dict[int, int], permutations: int, verbose: bool
) -> None:
    print("Statistics:")
    if verbose:
        print(f"Total possible permutations: {permutations}")
    for i, (k, v) in enumerate(frequency.items()):
        if verbose:
            # iteration, sample, observation
            print(f"i: {i + 1}, s: {k}, o: {v}")
        else:
            print(f"sample: {k}, observations: {v}")


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
        "-r",
        "--non-replacement",
        action="store_true",
        help="Enable non-replacement sampling. Defaults to False.",
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
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Output the distribution frequency. Defaults to False.",
    )
    return parser.parse_args()


def main():
    args = get_args()

    if args.non_replacement and args.size > (args.stop - args.start):
        print(
            f"Error: Cannot sample {args.size} elements from a population of {args.stop - args.start}"
        )
        return

    # Set a seed for deterministic output if the flag is set
    if args.deterministic:
        random.seed(args.seed)

    # Sample selected population
    sampler = get_sampler(args)
    frequency = get_sampled_frequency(sampler)
    print_sampled_frequency(frequency, sampler.permutations, args.verbose)


if __name__ == "__main__":
    main()

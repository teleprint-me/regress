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


@dataclasses.dataclass
class SamplerParameters:
    start: int
    stop: int
    size: int


class ReplacementSampler:
    def __init__(self, parameters: SamplerParameters):
        self.parameters = parameters
        self.population = list(range(parameters.start, parameters.stop))

    @property
    def population_size(self) -> int:
        return len(self.population)

    @property
    def permutations(self) -> int:
        """
        The formula for the number of permutations with replacement is j^n,
        where j is the population size and n is the sample size.
        """
        return int(pow(self.population_size, self.parameters.size))

    def repopulate(self) -> None:
        self.population = list(range(self.parameters.start, self.parameters.stop))

    def sample(self) -> int:
        return self.population[random.randrange(self.population_size)]

    def generate(self) -> Generator:
        for _ in range(self.parameters.size):
            yield self.sample()


class NonReplacementSampler(ReplacementSampler):
    @property
    def permutations(self) -> int:
        """
        The formula for permutations is (j! / (j - n)!), where j is the
        population size and n is the sample size.
        """
        # Ensure the population is large enough for the requested sample size
        if self.parameters.size > self.population_size:
            return 0
        return math.factorial(self.population_size) // math.factorial(
            self.population_size - self.parameters.size
        )

    def sample(self) -> Optional[int]:
        try:
            return self.population.pop(random.randrange(self.population_size))
        except (IndexError,):
            return None

    def generate(self) -> Generator:
        for _ in range(min(self.parameters.size, self.population_size)):
            yield self.sample()


def get_sampler(
    args: argparse.Namespace,
) -> Union[ReplacementSampler, NonReplacementSampler]:
    parameters = SamplerParameters(args.start, args.stop, args.size)
    if args.non_replacement:
        return NonReplacementSampler(parameters)
    return ReplacementSampler(parameters)


def get_sampled_frequency(
    sampler: Union[ReplacementSampler, NonReplacementSampler]
) -> Dict[int, int]:
    # Collect sampled frequency metadata
    frequency = {}
    for i, sample in enumerate(sampler.generate()):
        element = frequency.get(sample, 0)
        frequency[sample] = element + 1
    return frequency


def print_sampled_frequency(
    frequency: Dict[int, int], permutations: int, verbose: bool
) -> None:
    print("Statistics:")
    for i, (k, v) in enumerate(frequency.items()):
        if verbose:
            print(f"i: {i + 1}, p: {permutations}, s: {k}, o: {v}")
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

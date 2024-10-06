"""
Copyright (C) 2024 Austin Berrio

Module: linear.sampler

Generalized sampler function that maps a domain to a codomain of integers with
flexible parameters for range and transformation.
"""

from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
from random import randrange, seed
from typing import Callable, Generator, List


@dataclass
class SamplerBoundaries:
    lower: int
    upper: int


@dataclass
class SamplerParameters:
    """
    Generalized sampling parameters.
    """

    domain: SamplerBoundaries
    codomain: SamplerBoundaries
    magnitude: int
    f: Callable[[int], int]  # Transformation function


class Sampler:
    def __init__(self, params: SamplerParameters):
        self.params = params

    @property
    def domain_space(self) -> List[int]:
        return [
            randrange(self.params.domain.lower, self.params.domain.upper)
            for _ in range(self.params.magnitude)
        ]

    @property
    def codomain_space(self) -> List[int]:
        # Apply transformation function f
        return [self.params.f(x) for x in self.domain_space]

    def sample(self) -> List[int]:
        """Generate a sample space and apply the transformation."""
        # Clip to codomain bounds
        codomain_space = [
            max(self.params.codomain.lower, min(self.params.codomain.upper, x))
            for x in self.codomain_space
        ]
        return codomain_space

    def generate(self) -> Generator:
        for i in self.sample:
            yield i


def get_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("--seed", type=int, default=42, help="The initial seed")
    parser.add_argument(
        "--domain-lower", type=int, default=1, help="Lower bound of domain"
    )
    parser.add_argument(
        "--domain-upper", type=int, default=6, help="Upper bound of domain"
    )
    parser.add_argument(
        "--codomain-lower", type=int, default=10, help="Lower bound of codomain"
    )
    parser.add_argument(
        "--codomain-upper", type=int, default=100, help="Upper bound of codomain"
    )
    parser.add_argument(
        "--magnitude", type=int, default=10, help="Size of the sample space"
    )
    return parser.parse_args()


def main():
    args = get_args()

    seed(args.seed)

    # Create sampler parameters
    params = SamplerParameters(
        domain=SamplerBoundaries(lower=args.domain_lower, upper=args.domain_upper),
        codomain=SamplerBoundaries(
            lower=args.codomain_lower, upper=args.codomain_upper
        ),
        magnitude=args.magnitude,
        f=lambda x: x * args.codomain_lower,  # transformation function
    )

    # Create the sampler with the given parameters
    sampler = Sampler(params)

    # Generate the sample
    sample_result = sampler.sample()

    # Output the result
    print(f"Sampled codomain: {sample_result}")


if __name__ == "__main__":
    main()

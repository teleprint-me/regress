"""
Copyright (C) 2024 Austin Berrio

Module: linear.sampler

Generalized sampler function that maps a domain to a codomain of integers with
flexible parameters for range and transformation.
"""

from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
from random import randrange, seed
from typing import Callable, Generator, List, Set


@dataclass
class SamplerBoundary:
    lower: int
    upper: int

    def assert_boundary(self):
        # Inclusive
        assert self.lower >= 0, "Lower bound must be greater than 0"
        # Exclusive - mostly for consistency with python
        assert self.upper > self.lower, "Upper bound must be greater than lower bound"


@dataclass
class SamplerParameters:
    """
    Generalized sampling parameters.
    """

    domain: SamplerBoundary
    magnitude: int
    f: Callable[[int], int]  # Transformation function


class Sampler:
    def __init__(self, params: SamplerParameters):
        self.params = params

    @property
    def domain_space(self) -> List[int]:
        """The set of elements defining the input space."""
        return [i for i in range(self.params.domain.lower, self.params.domain.upper)]

    @property
    def codomain_space(self) -> List[int]:
        """The set of elements defining the output space."""
        return [self.params.f(x) for x in self.domain_space]

    def sample(self) -> int:
        """Select a replaceable sample from the codomain space."""
        return self.codomain_space[randrange(self.params.magnitude)]

    def generate(self) -> Generator:
        """Generate replaceable samples from the sampled space."""
        for _ in self.codomain_space:
            yield self.sample()


def get_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "-d",
        "--deterministic",
        action="store_true",
        help="Enable deterministic output.",
    )
    parser.add_argument(
        "-s",
        "--seed",
        type=int,
        default=42,
        help="Seed for deterministic output. Defaults to 42.",
    )
    parser.add_argument(
        "--domain-lower", type=int, default=1, help="Lower bound of domain"
    )
    parser.add_argument(
        "--domain-upper", type=int, default=6, help="Upper bound of domain"
    )
    return parser.parse_args()


def main():
    args = get_args()

    if args.deterministic:
        seed(args.seed)

    # Create sampler parameters
    params = SamplerParameters(
        domain=SamplerBoundary(lower=args.domain_lower, upper=args.domain_upper),
        magnitude=args.domain_upper - 1,
        f=lambda x: x * x,  # transformation function
    )

    params.domain.assert_boundary()

    # Create the sampler with the given parameters
    sampler = Sampler(params)

    # Generate the sample
    sample_result = sampler.sample()

    # Output the result
    print(f"Domain space: {sampler.domain_space}")
    print(f"Codomain space: {sampler.codomain_space}")
    print(f"Sampled codomain element: {sample_result}")


if __name__ == "__main__":
    main()

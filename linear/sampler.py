"""
Copyright (C) 2024 Austin Berrio

Module: linear.sampler

Generalized sampler function that maps a domain to a codomain of integers with
flexible parameters for range and transformation.
"""

from dataclasses import dataclass
from random import randrange
from typing import Callable, List


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


def main():
    # Define the transformation function
    f = lambda x: x * 10  # Example: multiply domain value by 10

    # Create sampler parameters
    params = SamplerParameters(
        domain=SamplerBoundaries(lower=1, upper=6),
        codomain=SamplerBoundaries(lower=10, upper=100),
        magnitude=10,
        f=f,
    )

    # Create the sampler with the given parameters
    sampler = Sampler(params)

    # Generate the sample
    sample_result = sampler.sample()

    # Output the result
    print(f"Sampled codomain: {sample_result}")


if __name__ == "__main__":
    main()

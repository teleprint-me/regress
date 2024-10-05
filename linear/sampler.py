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
class SamplerBoundary:
    upper: int
    lower: int


@dataclass
class SamplerParameters:
    """
    Generalized sampling parameters.
    """

    domain_lower: int
    domain_upper: int
    codomain_lower: int
    codomain_upper: int
    magnitude: int
    f: Callable[[int], int]  # Transformation function


class Sampler:
    def __init__(self, params: SamplerParameters):
        self.params = params

    def sample(self) -> List[int]:
        """Generate a sample space and apply the transformation."""
        domain_space = [
            randrange(self.params.domain_lower, self.params.domain_upper)
            for _ in range(self.params.magnitude)
        ]
        # Apply transformation function f
        codomain_space = [self.params.f(x) for x in domain_space]
        # Clip to codomain bounds
        codomain_space = [
            max(self.params.codomain_lower, min(self.params.codomain_upper, x))
            for x in codomain_space
        ]
        return codomain_space


def main():
    # Define the transformation function
    f = lambda x: x * 10  # Example: multiply domain value by 10

    # Create sampler parameters
    params = SamplerParameters(
        domain_lower=1,
        domain_upper=6,
        codomain_lower=10,
        codomain_upper=100,
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

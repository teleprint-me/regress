"""
Copyright (C) 2024 Austin Berrio

Module: linear.sampler

Generalized sampler function that maps a domain to a codomain of integers
with flexible parameters for range and transformation.
"""

from argparse import ArgumentParser, Namespace
from random import randrange
from typing import Callable


class SamplerParameters:
    """
    Generalized sampling parameters.

    Parameters:
    domain_lower: int - Lower bound of domain (input set)
    domain_upper: int - Upper bound of domain (input set)
    codomain_lower: int - Lower bound of codomain (output set)
    codomain_upper: int - Upper bound of codomain (output set)
    magnitude: int - Size of sample space
    f: Callable[[int], int] - Transformation function
    """

    domain_lower: int
    domain_upper: int
    codomain_lower: int
    codomain_upper: int
    magnitude: int
    f: Callable[[int], int]


class Sampler:
    pass


def sampler(params: SamplerParameters):
    """
    Generalized sampling function.

    Parameters:
    domain_lower: int - Lower bound of domain (input set)
    domain_upper: int - Upper bound of domain (input set)
    codomain_lower: int - Lower bound of codomain (output set)
    codomain_upper: int - Upper bound of codomain (output set)
    magnitude: int - Size of sample space
    f: Callable[[int], int] - Transformation function
    """
    # Generate the sample space from the domain
    domain_space = [randrange(domain_lower, domain_upper) for _ in range(magnitude)]

    # Apply the transformation function f to map domain -> codomain
    codomain_space = [f(x) for x in domain_space]

    # Clip to codomain bounds if necessary
    codomain_space = [
        max(codomain_lower, min(codomain_upper, x)) for x in codomain_space
    ]

    return codomain_space


def main():
    # Set up default domain and codomain bounds for demo purposes
    domain_lower = 1
    domain_upper = 6
    codomain_lower = 10
    codomain_upper = 100
    magnitude = 10

    # Simple transformation function: identity (no transformation)
    f = lambda x: x * 10  # Just a simple example, multiplies domain value by 10

    # Call sampler function
    result = sampler(
        domain_lower, domain_upper, codomain_lower, codomain_upper, magnitude, f
    )

    # Output results
    print(f"Sampled codomain: {result}")


if __name__ == "__main__":
    main()

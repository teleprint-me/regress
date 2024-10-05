"""
Script: linear.roll

Generate a set of a values for generating linear sequences

Generate a distribution set within a given range
"""

from random import randrange


def dice_roll() -> int:
    return [1, 2, 3, 4, 5, 6][randrange(1, 6)]


def main():
    # create a sample size of 10
    for i in range(10):
        print(f"i: {i}, roll: {dice_roll()}")


if __name__ == "__main__":
    main()

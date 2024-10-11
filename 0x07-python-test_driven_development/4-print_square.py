#!/usr/bin/python3
"""
A module that prints a square based on the input provided to a
function
"""


def print_square(size):
    """
    A function that prints a square

    Args:
        size (int): the size of the square to be printed
    Return:
        the square printed on the stdout

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


if __name__ == "__main__":
    import doctest
    doctest.testmod()

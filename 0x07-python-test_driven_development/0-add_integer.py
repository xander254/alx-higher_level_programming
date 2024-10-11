#!/usr/bin/python3
"""
This module provides a function to add two integers or floats.
The add_integer function takes two parameters and returns their sum
as an integer.
It raises TypeErrors for invalid input types.
Usage examples are included in the function's docstring.
Ensure that both parameters are either integers or floats.
"""


def add_integer(a, b=98):
    """
    A function that adds two intgers a and b
    Args:
        a (int, float): the first integer to be summed
        b (int, float): the second integer to be summed, if no
                        value defaults to 98

    Returns:
        int: the sum of the two numbers
    """
    """
    Examples:
        >>> add_integer(3, "cows")
        Traceback (most recent call last):
            ...
        TypeError: b must be an integer

        >>> add_integer("cat", 4)
        Traceback (most recent call last):
            ...
        TypeError: a must be an integer

        >>> add_integer(1, 2)
        3

        >>> add_integer(100, -2)
        98

        >>> add_integer(2)
        100

        >>> add_integer(100.3, -2)
        98

        >>> add_integer(-2, -4)
        -6

        >>> add_integer(10.56, 120.27)
        130

        >>> add_integer()
        Traceback (most recent call last):
            ...
        TypeError: add_integer() missing 1 required positional
        argument: 'a'
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()

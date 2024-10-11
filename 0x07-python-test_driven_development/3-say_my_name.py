#!/usr/bin/python3
"""
A module that prints "My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """
    a function that prints My name is <first name> <last name>

    Args:
        first_name (string): the string that is the first name
        last_name (string): the string that is the last name

    Returns:
        A string My name is <first name> <last name>
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testmod()

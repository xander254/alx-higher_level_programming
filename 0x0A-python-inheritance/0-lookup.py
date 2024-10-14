#!/usr/bin/python3
"""

A method that lists attributes of an object

"""


def lookup(obj):
    """

    A function that returns the list of available attributes and
    methods of an object

    Args:
        obj - an object to be evaluated

    Return: a list with the attributes
    """
    attributes = list(dir(obj))
    return attributes

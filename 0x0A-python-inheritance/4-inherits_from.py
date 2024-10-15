#!/usr/bin/python3
"""
A module that checks if object is an instance of a class
"""


def inherits_from(obj, a_class):
    """
    A function that checks if an object is an instance of a class
    Args:
        obj : object to be checked
        a_class : class to be checked against
    Return: True / False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

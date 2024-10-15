#!/usr/bin/python3
"""
A module that finds if an object is in a kind of class
"""


def is_kind_of_class(obj, a_class):
    """
     a function that returns True if the object is an instance of,
     or if the object is an instance of a class that inherited from,
     the specified class ; otherwise False.

    Args:
        obj : the object being evaluated
        a_class: the class that the object is being checked against
    Return: True / False
    """
    if (isinstance(obj, a_class)):
        return True
    else:
        return False

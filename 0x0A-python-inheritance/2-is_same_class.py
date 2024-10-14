#!/usr/bin/python3
"""
A module that finds if a value is in a certain class
"""


def is_same_class(obj, a_class):
    """
     a function that returns True if the object is exactly an
     instance of the specified class ; otherwise False

     Args:
        obj : the object to be checked
        a_class:  a class the object is checked against

       """
    if (isinstance(obj, a_class)):
        return True
    else:
        return False

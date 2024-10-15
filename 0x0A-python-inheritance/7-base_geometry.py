#!/usr/bin/python3
"""
A module that creates a base geometry class
"""


class BaseGeometry:
    """
    A class Base Geometry
    """
    def __init__(self, name="string", value=0):

        self.name = name
        self.value = value

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(" {} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.name = name
        self.value = value

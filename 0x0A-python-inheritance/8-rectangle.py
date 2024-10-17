#!/usr/bin/python3
"""
A module that creates a base geometry class
"""


class BaseGeometry:
    """
    A class Base Geometry
    """
    def __init__(self, name="string", value=0):
        """
        Initialize a BaseGeometry object.

        Args:
            name (str): The name of the geometry.
            value (int): The value associated with the geometry.

        """
        self.name = name
        self.value = value

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is an integer greater than 0.

        Args:
            name (str): The name of the parameter (for error messages).
            value (int): The value to validate.
        """
        if not isinstance(value, int):
            raise TypeError(" {} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class that inherits from base geometry
    """
    def __init__(self, width, height):
        """
         innit class
         args:
               width (int) width of rectangle
               height (int) height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.width = width

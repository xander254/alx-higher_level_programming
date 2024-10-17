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
        return Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(" {} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.name = name
        self.value = value


class Rectangle(BaseGeometry):
    """
    A class rectangle that inherits from basegeometry and creates
    a rectangle
    """
    def __init__(self, width, height):
        """
        Initialize a rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Return the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

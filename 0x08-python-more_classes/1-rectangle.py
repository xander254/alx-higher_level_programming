#!/usr/bin/python3
"""
A method that creates a class Rectangle
"""


class Rectangle:
    """
    A class representing a rectangle object
    """
    def __init__(self, width=0, height=0):
        """
        initiator
        :width (int) the width of the rectangle
        :height (int) the height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValuError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

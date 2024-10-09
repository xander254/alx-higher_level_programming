#!/usr/bin/python3
"""
A module that create a class Rectangle
"""


class Rectangle:
    """
    A class that represents a rectangle
    This class allows setting of height and width
    """
    def __init__(self, width=0, height=0):
        """
        initialization of a class Rectangle
        :param width: (int) the width of the rectangle
        :param height: (int) the height of the reactangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
        self.__height = value

    def area(self):
        """
        Returna area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns perimeter of rectangle
        if either height/ width == 0 perimeter is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        returns a string representation of a rectngle using #
        """
        if self.__width == 0 or self.__height == 0:
            return
        return "\n".join("#" * self.__width for _ in range(self.__height))

    def __repr__(self):
        """
        Return a string that represents a rectangle
        """
        return ("{}, {}".format(self.__width, self.__height))

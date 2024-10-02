#!/usr/bin/python3
"""
This module defines a Square class
"""


class Square:
    """
    A class that represents a square
    """
    def __init__(self, size=0):
        """
        Initialization of class square

        Args:
            size(int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Area method
        Args:
            self(class Square)
        """
        return self.__size * self.__size

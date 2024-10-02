#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    A class to represent a square.
    """
    def __init__(self, size=0):
        """
        Initialize a square object
        Args:
            size(int): The size of a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

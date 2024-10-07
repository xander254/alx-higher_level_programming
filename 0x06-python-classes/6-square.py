#!/usr/bin/python3
"""
A module that creates a class Square
"""
from shutil import get_terminal_size


class Square:
    """
    A class representing a square object
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        :size (int): size of the square
        :position (int) tupple showing the cordinated of printing
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.size * self.size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.size == 0:
            print()
            return
        for i in range(0, self.position[1]):
            print()
        for row in range(0, self.size - 1):
            print("{}".format(self.position[0] * " "), end="")
            print("#" * self.size)

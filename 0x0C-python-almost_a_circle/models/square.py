#!/usr/bin/python3
"""
A module that inherits a rectangle class in order to make a square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class square that inherits froma rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class squere initialization with values
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        a property that returns the size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        A dunder method that prints the state of the square
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.size}")

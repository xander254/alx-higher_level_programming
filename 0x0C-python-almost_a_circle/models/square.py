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

    def update(self, *args, **kwargs):
        """
        A method that updates the dimensions based on orgs & kwargs
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def display(self):
        """
        A public method to display the rectangle using #
        """
        for _ in range(self.y):
            print(" ")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width, end="\n")

    def __str__(self):
        """
        A dunder method that prints the state of the square
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.size}")

#!/usr/bin/python3
"""
A module that creates the first class
"""


class Base:
    """
    The base class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the class with an id attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def __str__(self):
        """
        retrun string represedntation of id
        Args:
            self.id (int): the id of te instance
        """
        return f"{self.id}"

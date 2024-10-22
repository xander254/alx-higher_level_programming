
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
        return f"{self.id}"

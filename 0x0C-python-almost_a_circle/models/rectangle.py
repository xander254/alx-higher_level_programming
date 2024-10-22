#!/usr/bin/python3
"""
A module that creates a class Rectangle and inherits some propertes
from the Base class
"""
from models.base import Base


class Rectangle(Base):
    """
    A class that represents a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialization of the class with private attributes
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Width getter
        """
        return self.__width

    @width.setter
    def width(self):
        """
        Width setter
        """
        self.__width = width

    @property
    def height(self):
        """
        Height getter
        """
        return self.__height

    @height.setter
    def height(self):
        """
        Height setter
        """
        self.__height = height

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self):
        """
        x setter
        """
        self.__x = x

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(Self):
        """
        y setter
        """
        self.__y = y

    def __str__(self):
        """
        Return a string representation of rectangle
        """
        return f"{self.id}"

#!/usr/bin/python3
"""
A module that create a class Rectangle
"""


class Rectangle:
    """
    A class that represents a rectangle
    This class allows setting of height and width
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0, print_symbol="#"):
        """
        initialization of a class Rectangle
        :param width: (int) the width of the rectangle
        :param height: (int) the height of the reactangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = print_symbol

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
            return ""
        return "\n".join(
                (str(self.print_symbol) * self.__width)
                for _ in range(self.__height)
        )

    def __repr__(self):
        """
        returns the repr representation of rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        delete an instance of a class
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def print__symbol(self):
        return Rectangle.print_symbol

    @print__symbol.setter
    def print__symbol(self, value):
        if isinstance(value, list):
            value = " ".join(value)
        Rectangle.print_symbol = value

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1 == rect_2:
            return True
        elif rect_1 > rect_2:
            return True
        else:
            return False

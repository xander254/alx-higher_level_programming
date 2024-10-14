#!/usr/bin/python3
"""
A module that creates a class that inherits from the class list
"""


class MyList(list):
    """
    A class that inherits from the class list
    """

    def __init__(self):
        """
        Initializing a class MyList
        Args:
            value (int): A value to be inputed by the user
        
        >>> my_list = MyList()
        >>> len(my_list)
        0
        """
        super().__init__()

    def print_sorted(self):
        """
        A mothod that prints the list but sorted in order

        Examples:
        >>> my_list = MyList()
        >>> my_list.append(1)
        >>> my_list.append(4)
        >>> my_list.append(2)
        >>> my_list.append(3)
        >>> my_list.append(5)
        >>> my_list.print_sorted()
        [1, 2, 3, 4, 5]

        """
        return sorted(self) 


if __name__ == "__main__":
    import doctest
    doctest.testmod()



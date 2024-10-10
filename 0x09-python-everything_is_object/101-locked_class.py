#!/usr/bin/python3


class LockedClass:
    """
    A locked class that cant allow creation of attributes
    """
    __slots__ = ['first_name']

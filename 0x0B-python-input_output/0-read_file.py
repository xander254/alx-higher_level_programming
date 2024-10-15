#!/usr/bin/python3
"""
A module that reads a text file and prints to stdout
"""


def read_file(filename=""):
    """
    A function that reads a text file (UTF8) and prints it to stdout
    Args:
        filename: the file name to be read
    Return: The data
    """
    with open('my_file_0.txt', encoding="utf-8") as f:
        print(f.read(), end="")

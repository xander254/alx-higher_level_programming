#!/usr/bin/python3
"""
A module that writes text to a file
"""


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file (UTF8) and return
    the number of characters written:
    Args:
        filename: the file name of the file that we are going to
        write
    """
    with open(filename, 'w', encoding="utf-8") as myFile:
        myFile.write(text)
    return len(text)

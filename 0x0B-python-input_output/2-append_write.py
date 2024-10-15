#!/usr/bin/python3
"""
A module that appends a string at the end of a file in utf-8 and
returns no of characters added
"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a text file
    (UTF8)and returns the number of characters added
    Args:
        filename: the file name that will be appended to
        text: the text to be appended
    """
    with open(filename, 'a', encoding="utf-8") as myFile:
        myFile.write(text)
    return len(text)

#!/usr/bin/python3
# A function that creates a cp of a string removing a character at
# n position
def remove_char_at(str, n):
    """
    A fuinction that removes a character at position n
    """
    if n < 0:
        return str
    length = len(str)
    string1 = str[0:n]
    string2 = str[n + 1:length]
    return string1 + string2

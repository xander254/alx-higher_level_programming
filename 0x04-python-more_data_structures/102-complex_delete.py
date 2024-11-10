#!/usr/bin/python3
# a function that deletes keys with a specific value in a dictionary
def complex_delete(a_dictionary, value):
    """
    a function that deletes keys with a specific value in a
    dictionary
    """
    delete_this = []

    if a_dictionary is None:
        return a_dictionary

    for key, val in a_dictionary.items():
        if val == value:
            delete_this.append(key)

    for key in delete_this:
        del a_dictionary[key]

    return a_dictionary

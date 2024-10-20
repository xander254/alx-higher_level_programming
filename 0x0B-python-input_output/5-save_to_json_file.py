#!/usr/bin/python3
"""
A module that writes an object to a file using json representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an Object to a text file, using a JSON
    representation
    Args:
        my_obj: A python onject
        filename: the file where the json rep will be saved
    """
    data = json.dumps(my_obj)

    with open(filename, 'w') as myJsonFile:
        myJsonFile.write(data)

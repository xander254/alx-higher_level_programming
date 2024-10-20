#!/usr/bin/python3
"""
A module that creates an object from a json file
"""
import json


def load_from_json_file(filename):
    """
    A func that creates an object froma json file
    Args:
        filename: The name of the json file
    """
    with open(filename, 'r') as myJsonFile:
        mydata = myJsonFile.read()
    my_obj = json.loads(mydata)
    return my_obj

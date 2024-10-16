#!/usr/bin/python3
import json
"""
A module that returns a JSON rep fo an object
"""


def to_json_string(my_obj):
    """
     a function that returns the JSON representation of an object
     (string)
     Args:
        my_obj: object to be turned to json
    """
    file = json.dumps(my_obj)
    return file

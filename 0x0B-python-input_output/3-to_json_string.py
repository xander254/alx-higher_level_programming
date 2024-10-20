#!/usr/bin/python3
"""
A module that returns a JSON rep fo an object
"""
import json


def to_json_string(my_obj):
    """
     a function that returns the JSON representation of an object
     (string)
     Args:
        my_obj: object to be turned to json
    """
    json_file = json.dumps(my_obj, sort_keys=True, indent=2)
    return json_file

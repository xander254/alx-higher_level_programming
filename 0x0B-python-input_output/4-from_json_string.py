#!/usr/bin/python3
"""
A module that uses json to convert a json string to an object
"""
import json


def from_json_string(my_str):
    """
    A function that retruns a py obj represented by a json string
    Args:
        my_str: the json string that will be used
    """
    loaded = json.loads(my_str)
    return loaded

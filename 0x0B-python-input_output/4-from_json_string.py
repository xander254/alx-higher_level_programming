#!/usr/bin/python3
import json


def from_json_string(my_str):
    """
    A function that retruns a py obj represented by a json string
    """
    dump = json.loads(my_str)
    return dump

#!/usr/bin/python3
"""
A module that creates the first class
"""
import json


class Base:
    """
    The base class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the class with an id attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def __str__(self):
        """
        retrun string represedntation of id
        Args:
            self.id (int): the id of te instance
        """
        return f"{self.id}"

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        a static mehod that returns jso representation of
        listdictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        A class methood that writes the json representation of
        list_objs to a file
        """
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_dicts = []
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)

        with open(filename, "w") as theFile:
            theFile.write(json_string)

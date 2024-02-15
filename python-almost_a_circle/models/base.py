#!/usr/bin/python3
"""
define a class Base.
"""

import json


class Base:
    """
    this a class that define a private class atribute.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor that initialize
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method that returns the json string.
        """
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that writes the json string representation
        of list_objs to a file.
        """
        filename = cls.__name__ + ".json"
        dictionary = []
        if list_objs is None:
            list_dicts = []
        else:
            dictionary = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(dictionary))

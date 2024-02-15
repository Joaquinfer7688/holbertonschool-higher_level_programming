#!/usr/bin/python3
"""
define a class Base.
"""

import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """
        static method that returns the list of the json string
        representation json_string.
        """
        if not json_string or json_string is None:
            return []
        else:
            return json.loads(json_string)

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

    @classmethod
    def create(cls, **dictionary):
        """
        class method that return an instance with all atributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        class method that return a list of instances.
        """
        filename = cls.__name__ + ".json"

        if not path.exists(filename):
            return []

        with open(filename, "r") as file:
            objs = cls.from_json_string(file.read())

        instances = []
        for element in objs:
            instances.append(cls.create(**element))
        return instances

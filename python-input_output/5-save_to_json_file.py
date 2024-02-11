#!/usr/bin/python3
"""
define a function that writes an object.
"""
import json


def save_to_json_file(my_obj, filename):
    """
     function that writes an Object to a text file,
     using a JSON representation.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return json.dump(my_obj, file)

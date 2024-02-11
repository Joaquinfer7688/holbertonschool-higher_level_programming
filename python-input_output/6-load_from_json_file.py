#!/usr/bin/python3
"""
define a function that creates an object.
"""
import json


def load_from_json_file(filename):
    """
     function that creates an Object from a “JSON file”.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

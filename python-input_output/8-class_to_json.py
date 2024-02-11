#!/usr/bin/python3
"""
define a function that return de dictionary.
"""


def class_to_json(obj):
    """
     function that returns the dictionary description with simple data
     structure (list, dictionary, string, integer and boolean)
     for JSON serialization of an object.
    """
    return obj.__dict__

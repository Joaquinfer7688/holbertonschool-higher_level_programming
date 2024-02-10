#!/usr/bin/python3
"""
Module that define a is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
    Function that return returns True if the object is an instance and otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

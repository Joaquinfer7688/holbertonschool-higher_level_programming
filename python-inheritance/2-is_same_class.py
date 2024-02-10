#!/usr/bin/python3
"""
Module that check if obj is a_class or an instance.
"""


def is_same_class(obj, a_class):
    """
    Function returns True if the object is exactly an instance or false.
    """
    if type(obj) is a_class:
        return True
    else:
        return False

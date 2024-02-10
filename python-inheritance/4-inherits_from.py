#!/usr/bin/python3
"""
This module define inherits_from.
"""


def inherits_from(obj, a_class):
    """
    Function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ;
    otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    elif type(obj) is not a_class:
        return True
    return False

#!/usr/bin/python3
"""
define a class Base.
"""


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

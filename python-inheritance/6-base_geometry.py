#!/usr/bin/python3
"""
This module define a function.
"""


class BaseGeometry:
    """
    class named BaseGeometry.
    """
    def area(self):
        """
        This a public instance method that raises
        an Exception with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

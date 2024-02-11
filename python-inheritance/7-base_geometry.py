#!/usr/bin/python3
"""
Thid method define BaseGeometry.
"""


class BaseGeometry:
    def area(self):
        """
        This a public instance method that raises
        an Exception with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Is a public instance method that validate the value.
        """
        if not isinstance(value, int):
            raise TypeError("f{name} must be an integer")
        if value <= 0:
            raise ValueError("f{name} must be greater than 0")

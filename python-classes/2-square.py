#!/usr/bin/python3
"""
This class define a square
"""


class Square:
    """
    This class represents a square.
    Attributes:
    Size: size of square.
    """
    def __init__(self, sixe=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be a >= 0")
        self.__size = size

#!/usr/bin/python3
"""
This class define a square
"""


class Square:
    """
    This class define a square
    Attributes:
        size: size of square
    """
    def __init__(self, size=0):
        if not insistance(size, int):
            raise TypeError("size must be ain integer")
        elif size < 0:
            raise ValueError("size must be a >= 0")
    def area(self):
        """
        This public instance method calculate the square area
        """
        return self.__size ** 2

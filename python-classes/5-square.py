#!/usr/bin/python3
"""
This class represent a square
"""


class Square:
    """
    This class creates a square
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(self.__size):
            for a in range(self.__size):
                print("#", end="")
            print()

        elif self.__size == 0:
            print()

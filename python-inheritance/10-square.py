#!/usr/bin/python3
"""
This module create a class based on BaseGeometry.
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
        function that validate a integer value.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
     class that define a Rectangle that inherits from BaseGeometry
    with height and width.
    """

    def __init__(self, width, height):
        """
        function that initialize a Rectangle with height and width.
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__widht * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    This a class Square that inherits from Rectangle.
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        function that calculate area of square.
        """
        return self.__size * self.__size

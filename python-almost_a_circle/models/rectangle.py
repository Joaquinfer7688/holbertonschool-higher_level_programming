#!/usr/bin/python3
"""
define a class Rectangle.
"""


from models.base import Base


class Rectangle(Base):
    """
    class that inherits from Base.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor that initialize.
        """
        super().__init__(id)
        self.width = width
        self.eight = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = y

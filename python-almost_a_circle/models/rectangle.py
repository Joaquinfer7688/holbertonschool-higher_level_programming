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
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        function that define area of rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        for i in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """
        method so that it returns
        """
        return f"[Rectangle] () {}/{} - {}/{}"
        .format(self.width, self.height, self.id, self.x, self.y)

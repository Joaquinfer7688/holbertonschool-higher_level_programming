#!/usr/bin/python3
"""
define a class Square.
"""


from models.rectangle import Rectangle


class Rectangle(Base):
    """
    class that inherits from Base.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor that initialize.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """
        method so that it returns a string.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
        .format(self.id, self.x, self.y, self.width, self.height))


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        class constructor that initialize.
        """
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """
        Returns a formatted string representation of the square.
        """
        return ("[Square] ({}) {}/{} - {}"
        .format(self.id, self.x, self.y, self.width))

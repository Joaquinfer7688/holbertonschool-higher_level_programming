#!/usr/bin/python3
"""
define a class Square.
"""


from models.rectangle import Rectangle


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

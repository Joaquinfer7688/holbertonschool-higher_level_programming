#!/usr/bin/python3
"""
define a class Square.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        class constructor that initialize
        """
        Rectangle.__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

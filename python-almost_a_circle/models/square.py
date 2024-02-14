#!/usr/bin/python3
"""
define a class Square.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class inherits from rectangle.
    """
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

    @property
    def size(self):
        """
        class Square by adding the public getter and setter size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        function that define a size.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        public method that assign attributes.
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        public method that return the dictionary
        representation of a Rectangle.
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

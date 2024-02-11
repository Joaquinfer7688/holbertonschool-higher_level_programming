#!/usr/bin/python3
"""

"""


class Student:
    """
    class that define a student by first name, last name and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        function that initialize a student.
        """
        self.first_name = first_name
        self.last_name - last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionary representation
        of a Student instance.
        """
        if attrs in None:
            return self.__dict__
        else:
            result_json = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result_json[attr] = getattr(self, attr)
            return result_json

#!/usr/bin/python3
"""
define a class student.
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
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        public method that retrieves a dictionary representation of a
        Student instance.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }

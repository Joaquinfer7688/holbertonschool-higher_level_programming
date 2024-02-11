#!/usr/bin/python3
"""
This module define class MyList.
"""


class MyList(list):
    """
    Class that inherits from list.
    """
    def print_sorted(self):
        """
        This public instance method that print the list.
        """
        sorted_list = sorted(self)
        print(sorted(self))

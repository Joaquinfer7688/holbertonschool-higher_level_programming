#!/usr/bin/python3
"""
Define a function that read a file.
"""


def read_file(filename=""):
    """
    function that reads a text file and prints it to stdout.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(line, end="")

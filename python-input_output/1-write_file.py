#!/usr/bin/python3
"""
define a function that write a string.
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8) and returns the
    number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        num_chars_written = file.write(text)
        return num_chars_written

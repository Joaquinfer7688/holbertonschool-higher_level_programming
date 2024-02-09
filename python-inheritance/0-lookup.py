#!/usr/bin/python3
"""
This a module define a function return attributes and methods
"""


def lookup(obj):
	"""
	Function return a list of available attributes and methods of an object
	"""
	return dir(obj)

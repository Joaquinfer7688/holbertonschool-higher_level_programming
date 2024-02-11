#!/usr/bin/python3
"""
define a script that adds all arguments to a Python list,
and then save them to a file.
"""

from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
try:
    list = load_from_json_file(filename)
except Exception:
    list = []

for i in range(1, len(argv)):
    list.append(argv[i])

save_to_json_file(list, filename)

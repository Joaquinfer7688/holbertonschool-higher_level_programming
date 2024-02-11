#!/usr/bin/python3
"""
define a pascal_triangle.
"""


def pascal_triangle(n):
    """
    function that returns a list of lists of
    integers representing the Pascal’s triangle of n.
    """
    if n <= 0:
        return ""

     triangle = [[1]]
    for current_row in range(1, n):
        row = [1]
        previous_row = triangle[current_row - 1]
        for element in range(1, current_row):
            row.append(previous_row[element] + previous_row[element - 1])
        row.append(1)
        triangle.append(row)
    return triangle

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
        return []
    triangle = [[1]]

    for a in range(1, n):
        l_row = triangle[-1]
        n_row = [1]

        for b in range(1, a):
            n_val = l_row[b-1] + l_row[b]
            n_row.append(n_val)

        n_row.append(1)
        triangle.append(n_row)

    return triangle

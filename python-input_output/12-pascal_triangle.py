#!/usr/bin/python3
"""

"""


def pascal_triangle(n):
    """
    function that returns a list of lists of
    integers representing the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]

        for j in range(1, i):
            val = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(val)
        row.append(1)
        triangle.append(row)

    return triangle

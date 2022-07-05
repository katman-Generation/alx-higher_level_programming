#!/usr/bin/python3
"""Module 12-pascal_triangle.
Returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Returns the pascal triangle of n.
    Returns: a list of list of integers
    """

    if n <= 0:
        return []

    p = [[0 for x in range(i + 1)] for i in range(n)]
    p[0] = [1]

    for i in range(1, n):
        p[i][0] = 1
        for j in range(1, i + 1):
            if j < len(p[i - 1]):
                p[i][j] = p[i - 1][j - 1] + p[i - 1][j]
            else:
                p[i][j] = p[i - 1][0]
    return p

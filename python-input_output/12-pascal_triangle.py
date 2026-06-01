#!/usr/bin/python3
"""Module for creating Pascal's triangle."""


def pascal_triangle(n):
    """Return Pascal's triangle as a list of lists."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        previous_row = triangle[i - 1]
        new_row = [1]

        for j in range(len(previous_row) - 1):
            new_row.append(previous_row[j] + previous_row[j + 1])

        new_row.append(1)
        triangle.append(new_row)

    return triangle

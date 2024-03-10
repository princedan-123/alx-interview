#!/usr/bin/python3

""" A programs that implements Pascal's triangle."""


triangle = []


def baseline():
    """Creates the first two rows of the Pascal's triangle."""
    global triangle
    triangle.append([1])
    triangle.append([1, 1])


def sum_item(item, row):
    """Creates a new row from the sum of the row above."""
    for index, value in enumerate(row):
        if value == item and index < len(row) - 1:
            next_item = row[index + 1]
            return item + next_item


def pascal_triangle(n):
    """A function that implements Pascal's triangle.
        Args:
            n: an integer that represents the size of the triangle.
        Return:
            A list of lists is returned with each inner
            list representing a row in the triangle.
    """
    global triangle
    if n <= 0:
        return []
    if n == 1:
        triangle.append([1])
    if n == 2:
        baseline()
    if n > 2:
        baseline()
        size = n - 2
        for num in range(0, size):
            copy = triangle[:]
            last_row = copy[-1]
            new_row = [
                    sum_item(value, last_row)
                    for index, value in enumerate(last_row)
                    if index != len(last_row) - 1
                    ]
            new_row.append(1)
            new_row.insert(0, 1)
            triangle.append(new_row)
    return triangle

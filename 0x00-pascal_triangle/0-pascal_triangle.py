#!/usr/bin/python3

""" A programs that implements Pascal's triangle."""


triangle = []


def baseline():
    """Creates the first two rows of the Pascal's triangle."""
    global triangle
    triangle.append([1])
    triangle.append([1, 1])


def create_row(row):
    """Creates a new row from the sum of the row above."""
    last_index = len(row) - 1
    new_row = []
    for index in range(0, len(row)):
        if index < last_index:
            next_index = index + 1
            value = row[index] + row[next_index]
            new_row.append(value)
    return new_row


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
            new_row = create_row(last_row)
            new_row.insert(0, 1)
            new_row.append(1)
            triangle.append(new_row)
    return triangle

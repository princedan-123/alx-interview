#!/usr/bin/python3
"""A module which transposes a 2d matrix."""


def rotate_2d_matrix(matrix):
    """
    A function that rotates an n xn 2d matrix clockwise.
    args:   matrix(list of lists), the matrix to be rotated.
            it is assumed the matrix will not be None
    return: None as the matrix is edited in place.
    """
    rotate_matrix = []
    for i in range(len(matrix)):
        init = []
        for col in matrix:
            init.append(col[i])
        init.reverse()
        rotate_matrix.append(init)
    for i in range(len(matrix)):
        matrix[i] = rotate_matrix[i]

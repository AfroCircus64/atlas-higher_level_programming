#!/usr/bin/python3
"""Defines a function that will divide a matrix"""


def matrix_divided(matrix, div):
    """Function to divide the matrix"""
    row_size = None

    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)\
                         of integers/floats")

    for i in matrix:
        if not i or not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists)\
                             of integers/floats")

        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("matrix must be a matrix (list of lists)\
                                 of integers/floats")

        if row_size is None:
            row_size = len(i)
        elif row_size != len(i):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]

    return new_matrix

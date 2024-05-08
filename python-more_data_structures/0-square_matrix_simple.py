#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    i = [[j ** 2 for j in row] for row in matrix]
    return i

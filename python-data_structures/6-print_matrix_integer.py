#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        for element in row:
            i += 1
            print("{:d}".format(element), end=(" " if i < len(row) else ""))
        print()

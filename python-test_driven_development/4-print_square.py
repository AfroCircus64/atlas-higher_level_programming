#!/usr/bin/python3
"""Defines a function to print a square"""


def print_square(size):
    """Prints a square using the character '#' """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print('', end='')
    else:
        for _ in range(size):
            for _ in range(size):
                print('#', end='')
            print()

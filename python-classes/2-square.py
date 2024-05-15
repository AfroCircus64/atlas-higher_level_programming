#!/usr/bin/python3
"""Defines the class square"""


class Square:
    """Class to define a square"""
    def __init__(self, size=0):
        """Creates the square"""
        self.__size = size

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

#!/usr/bin/python3
"""Defines the class square"""


class Square:
    """Class to define a square"""
    def __init__(self, size=0):
        """Creates the square"""
        self.size = size

    @property
    def size(self):
        """Getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' characters."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

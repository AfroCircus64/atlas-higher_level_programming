#!/usr/bin/python3
"""Defines the class square"""


class Square:
    """Class to define a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Creates the square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if not isinstance(position, tuple) or len(position)!= 2 or \
           not isinstance(position[0], int) or not isinstance(position[1], int) or \
           position[0] <= 0 or position[1] <= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """Gets the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square."""
        if not isinstance(value, tuple) or len(value)!= 2 or \
           not isinstance(value[0], int) or not isinstance(value[1], int) or \
           value[0] <= 0 or value[1] <= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__position[0]):
                print(" " * self.__position[0], end="")
            for _ in range(self.__size):
                print("#", end="")
            print()

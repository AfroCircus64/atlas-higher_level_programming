#!/usr/bin/python3
"""Defines a class that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a class called Square"""

    def __init__(self, size):
        """Initializes the Square"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the Square"""

        return self.__size ** 2

#!/usr/bin/python3
"""Defines a class that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a class called Rectangle"""

    def __init__(self, width, height):
        """Initialize the Rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Defines an area method"""

        return self.__width * self.__height

    def __str__(self):
        """Returns the next string"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

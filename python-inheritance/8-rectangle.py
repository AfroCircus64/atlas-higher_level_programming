#!/usr/bin/python3
"""Defines a class that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseException):
    """Defines a class called Rectangle"""

    def __init__(self, width, height):
        """Initialize the Rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._Rectangle__width = width
        self._Rectangle__height = height

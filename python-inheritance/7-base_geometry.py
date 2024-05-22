#!/usr/bin/python3
"""Defines a class called BaseGeometry"""


class BaseGeometry():
    """Empty class"""

    def area(self):
        """public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value passed as an argument."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

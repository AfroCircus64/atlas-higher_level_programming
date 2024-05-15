#!/usr/bin/python3
"""Defines the class add_integer"""
def add_integer(a, b=98):
    """Class to add two integers"""
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return int(a) + int(b)
        else:
            raise TypeError("a must be an integer or b must be an integer")
    except ValueError:
        raise TypeError("a must be an integer or b must be an integer")

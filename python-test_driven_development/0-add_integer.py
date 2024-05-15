#!/usr/bin/python3
"""Defines the class add_integer"""
def add_integer(a, b=98):
    """Class to add two integers"""
    if type(a) is not int:
        raise TypeError("a must be an integer")
    elif type(a) is float:
        a = int(a)
    if type(b) is not int:
        raise TypeError("b must be an integer")
    elif type(b) is float:
        b = int(b)
    return a + b

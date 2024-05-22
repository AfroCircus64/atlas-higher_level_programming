#!/usr/bin/python3
"""Defines a func that checks for an inherited instance"""


def inherits_from(obj, a_class):
    """Function to check for instance"""

    return False if type(obj) is a_class else isinstance(obj, a_class)

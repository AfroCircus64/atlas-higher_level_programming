#!/usr/bin/python3
"""Defines a class - class_to_json"""


def class_to_json(obj):
    """function that returns the description  for JSON"""

    return vars(obj)

#!/usr/bin/python3
"""Defines a func - to_json_string"""


import json


def to_json_string(my_obj):
    """function that returns the JSON representation of a string"""

    return json.dumps(my_obj)

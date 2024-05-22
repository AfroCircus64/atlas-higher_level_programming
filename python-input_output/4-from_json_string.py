#!/usr/bin/python3
"""Defines a func - from_json_string"""


import json


def from_json_string(my_str):
    """function that returns an object as a JSON string"""

    return json.loads(my_str)

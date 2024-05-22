#!/usr/bin/python3
"""Defines a func - load_from_json_file"""


import json


def load_from_json_file(filename):
    """function that creates an Object from a JSON file"""

    with open(filename, encoding='utf-8') as reader:
        return json.load(reader)

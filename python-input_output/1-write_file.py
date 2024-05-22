#!/usr/bin/python3
"""Defines a func - write_file"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file"""

    with open(filename, encoding='utf-8') as reader:
        return len(reader.readlines())

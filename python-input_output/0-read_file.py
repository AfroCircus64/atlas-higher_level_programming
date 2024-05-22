#!/usr/bin/python3
"""Defines a func - read_file"""


def read_file(filename=""):
    """Function that reads a text file"""

    with open(filename, encoding='utf-8') as reader:
        print(reader.read(), end="")

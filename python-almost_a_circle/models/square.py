#!/usr/bin/python3
"""
Defines a Square class that inherits from Rectangle.
"""

import json

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a Square class that inherits from Rectangle.
    
    Attributes:
        size (int): Size of the square.
    """
    def __init__(self, **kwargs):
        """initializes the square"""
        super().__init__(**kwargs)
        self.size = kwargs.get('size')

    @property
    def size(self):
        """returns the width"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        self.width = value

    def __str__(self):
        """format of the square returns"""
        return "Square({}, {}, {}, {})".format(self.size, self.x, self.y, self.id)

    def to_dictionary(self):
        """dict for the parameters of the square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    @classmethod
    def create(cls, **kwargs):
        """create func"""
        return cls(**kwargs)

    @classmethod
    def save_to_file(cls, list_objs=None, filename="squares.json"):
        """save to file func"""
        if list_objs is None:
            list_objs = []
        with open(filename, 'w') as f:
            json.dump([obj.to_dictionary() for obj in list_objs], f)

    @classmethod
    def load_from_file(cls, filename="squares.json"):
        """load from file func"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            return [cls(**item) for item in data]
        except FileNotFoundError:
            return []

#!/usr/bin/python3

import json

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = kwargs.get('size')

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def __str__(self):
        return "Square({}, {}, {}, {})".format(self.size, self.x, self.y, self.id)

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    @classmethod
    def create(cls, **kwargs):
        return cls(**kwargs)

    @classmethod
    def save_to_file(cls, list_objs=None, filename="squares.json"):
        if list_objs is None:
            list_objs = []
        with open(filename, 'w') as f:
            json.dump([obj.to_dictionary() for obj in list_objs], f)

    @classmethod
    def load_from_file(cls, filename="squares.json"):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            return [cls(**item) for item in data]
        except FileNotFoundError:
            return []

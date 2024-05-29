#!/usr/bin/python3

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

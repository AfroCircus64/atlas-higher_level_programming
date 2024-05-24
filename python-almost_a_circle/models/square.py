#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

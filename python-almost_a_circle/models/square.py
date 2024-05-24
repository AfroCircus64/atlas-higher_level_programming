#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, *args):
        super().__init__(*args)
        self.size = self.width

    def __str__(self):
        return ("Square({}, {}, {})".format(self.size, self.x, self.y))

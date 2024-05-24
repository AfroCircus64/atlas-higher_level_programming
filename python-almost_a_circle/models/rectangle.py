#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    def __init__(self, *args):
        super().__init__()
        self.width = args[0]
        self.height = args[1] if len(args) > 1 else 1
        self.x = args[2] if len(args) > 2 else 0
        self.y = args[3] if len(args) > 3 else 0

    def area(self):
        return self.width * self.height

    def __str__(self):
        return ("Rectangle({}, {}, {},\
                 {})".format(self.width, self.height, self.x, self.y))

    def display(self):
        print("Displaying rectangle with width={}, height={}, x={},\
                y={}".format(self.width, self.height, self.x, self.y))

    def to_dictionary(self):
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def update(self, *args, **kwargs):
        for key, value in kwargs.items():
            if key in ['width', 'height']:
                if not isinstance(value, int) or value <= 0:
                    raise ValueError(f"{key} must be a positive integer.")
            setattr(self, key, value)

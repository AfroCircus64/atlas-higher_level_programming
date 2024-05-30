#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from Base.
"""

import json

from models.base import Base


class Rectangle(Base):
    """
    Defines a Rectangle class that inherits from Base.
    
    Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
        __x (int): X coordinate of the rectangle.
        __y (int): Y coordinate of the rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)

    @property
    def height(self):
        return (self.__height)

    @property
    def x(self):
        return (self.__x)

    @property
    def y(self):
        return (self.__y)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @classmethod
    def create(cls, **kwargs):
        """create func"""
        return cls(**kwargs)

    @staticmethod
    def save_to_file(list_objs, filename='rectangles.json'):
        """save to file func"""
        if list_objs is None:
            list_objs = []
        with open(filename, 'w') as f:
            json.dump([obj.to_dictionary() for obj in list_objs], f)

    @classmethod
    def load_from_file(cls, filename='rectangles.json'):
        """load from file func"""
        try:
            with open(filename, 'r') as f:
                objs_data = json.load(f)
            return [cls(**item) for item in objs_data]
        except FileNotFoundError:
            return []

    def area(self):
        """returns the area"""
        return self.width * self.height

    def __str__(self):
        """format of the rectangle returns"""
        return ("Rectangle({}, {}, {},\
 {})".format(self.width, self.height, self.x, self.y))

    def display(self):
        """displays the rectangle"""
        print("Displaying rectangle with width={}, height={}, x={}, y={}".format(
            self.width, self.height, self.x, self.y))

    def to_dictionary(self):
        """dict for the parameters"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def update(self, *args, **kwargs):
        """updates the rectangle"""
        for key, value in kwargs.items():
            if key in ['width', 'height']:
                if not isinstance(value, int) or value <= 0:
                    raise ValueError(f"{key} must be a positive integer.")
            setattr(self, key, value)

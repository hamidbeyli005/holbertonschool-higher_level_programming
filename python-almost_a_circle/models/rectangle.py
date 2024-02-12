#!/usr/bin/python3
"""Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer('width', value, False)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer('height', value, False)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer('x', value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer('y', value)
        self.__y = value

    @staticmethod
    def validate_integer(name, value, equal = True):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer.'.format(name))
        if equal and value < 0:
            raise ValueError('{} must be > 0'.format(name))
        elif not equal and value <= 0:
            raise ValueError('{} must be >= 0'.format(name))

    def area(self):
        return self.__width * self.__height

    def display(self):
        for i in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        return '[{}] ({}) {}/{} - {}/{}'.format(self.__class__.__name__, self.id, self.__x, self.__y, self.__width, self.__height)

#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """A class to represent a rectangle."""
    def __init__(self, width=0, height=0):
        """init rectangle
        Args:
            width: the width
            height: the height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return rectangle area"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return area"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ''
        for _ in range(self.__height):
            rectangle_str += '#' * self.__width + '\n'
        return rectangle_str[:-1]

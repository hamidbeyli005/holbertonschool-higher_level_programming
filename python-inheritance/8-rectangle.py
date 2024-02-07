#!/usr/bin/python3
"""Module 8-rectangle.
Creates a Rectangle class.
"""


BaseGeometr = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class""

    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

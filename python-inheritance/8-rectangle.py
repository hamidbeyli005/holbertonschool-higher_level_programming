#!/usr/bin/python3
"""Module 8-rectangle.
Creates a Rectangle class.
"""


BaseGeometr = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle.
    Private instance attributes:
        - width
        - height
    Inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """Rectangle init method"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

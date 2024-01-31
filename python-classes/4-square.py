#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Initialize a square with a given size.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Calculate and return the current square area."""
        return self.__size ** 2

    @property
    def size(self):
        """Getter function"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

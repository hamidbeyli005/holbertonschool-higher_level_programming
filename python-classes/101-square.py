#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """This class represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a given size.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        if (not isinstance(position, tuple) or len(position) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in position)):

            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    def my_print(self):
        """Print Square"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """Position Getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """Position Setter"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):

            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """Return Square"""
        result = ""
        if self.__size == 0:
            result += "\n"
        else:
            for _ in range(self.__position[1]):
                result += "\n"
            for _ in range(self.__size):
                result += (" " * self.__position[0] + "#" * self.__size + "\n")
        return result

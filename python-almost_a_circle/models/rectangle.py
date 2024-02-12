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
        """int: Width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width value to set.
        """
        self.validate_integer('width', value, False)
        self.__width = value

    @property
    def height(self):
        """int: Height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height value to set.
        """
        self.validate_integer('height', value, False)
        self.__height = value

    @property
    def x(self):
        """int: X-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle.

        Args:
            value (int): The x-coordinate value to set.
        """
        self.validate_integer('x', value)
        self.__x = value

    @property
    def y(self):
        """int: Y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle.

        Args:
            value (int): The y-coordinate value to set.
        """
        self.validate_integer('y', value)
        self.__y = value

    def validate_integer(self, name, value, equal=True):
        """Validate an integer value.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to validate.
            equal (bool, optional): Whether the value can be equal
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to zero
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer.'.format(name))
        if equal and value < 0:
            raise ValueError('{} must be >= 0'.format(name))
        elif not equal and value <= 0:
            raise ValueError('{} must be > 0'.format(name))

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle."""
        for _ in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return '[{}] ({}) {}/{} - {}/{}'.format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)

    def update(self, *args, **kvargs):
        """Update the rectangle's attributes."""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kvargs.items():
                setattr(self, key, value)

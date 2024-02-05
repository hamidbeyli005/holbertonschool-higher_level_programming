#!/usr/bin/python3
"""Rectangle module"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """My Square Class"""
    def __init__(self, size):
        """Init method"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Area method override"""
        return self.__size ** 2

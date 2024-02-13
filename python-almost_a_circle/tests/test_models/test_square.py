#!/usr/bin/python3
"""Square test module"""


import unittest
from models.square import Square


class TestBase(unittest.TestCase):
    def test_square_positive_num(self):
        square = Square(1, 2, 3, 4)
        self.assertEquals(square.size, 1)

        square = Square(1, 2, 3)
        self.assertEquals(square.size, 1)

        square = Square(1, 2)
        self.assertEquals(square.size, 1)

    def test_square_string(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square("1")

    def test_value_error(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(-1)

    def test_str(self):
        square = Square(1, id=1)
        self.assertEqual(str(square), "[Square] (1) 0/0 - 1")

    def test_to_dictionary(self):
        square = Square(10, 2, 1, 1)
        self.assertEqual(
                square.to_dictionary(), {'id': 1, 'x': 2, 'size': 10, 'y': 1})

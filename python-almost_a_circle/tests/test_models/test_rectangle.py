#!/usr/bin/python3
"""Rectangle test module"""


import unittest
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    def test_rectangle(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)


if __name__ == "__main__":
    unittest.main()

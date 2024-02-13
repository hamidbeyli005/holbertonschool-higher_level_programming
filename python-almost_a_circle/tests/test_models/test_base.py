#!usr/bin/python3
"""Unit test"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    def test_id(self):
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base(None)
        self.assertEqual(b.id, 2)


if __name__ == '__main__':
    unittest.main()



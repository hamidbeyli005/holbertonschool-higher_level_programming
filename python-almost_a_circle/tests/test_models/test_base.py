#!usr/bin/python3
"""Unit test"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def test_id_as_positive(self):
        b= Base(115)
        self.assertEqual(b.id, 115)
        #b = Base(67)
        #self.assertEqual(b.id, 67)

    def test_id_as_negative(self):
        b = Base(-91)
        self.assertEqual(b.id, -91)
        #b = Base(-4)
        #self.assertEqual(b.id, -4)

    def test_id(self):
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base(None)
        self.assertEqual(b.id, 2)


if __name__ == '__main__':
    unittest.main()



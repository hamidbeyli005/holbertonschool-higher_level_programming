#!/usr/bin/python3
"""Rectangle test module"""


import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestBase(unittest.TestCase):
    def test_rectangle(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.id, 5)
    
    def test_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.area(), 2)

    def test_str(self):
        rect = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(rect.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_display(self):
        # Create a rectangle
        rectangle = Rectangle(3, 4)

        # Expected output
        expected_output = "###\n" * 4

        # Check if the display method provides the correct output when called
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rectangle.display()
            self.assertEqual(fake_out.getvalue(), expected_output)
        
        rectangle = Rectangle(2, 3, 1, 1)
        expected_output = "\n ##\n ##\n ##\n"
        # Check if the display method provides the correct output when called
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rectangle.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_to_dictionary(self):
        rect = Rectangle(10, 2, 1, 9)
        self.assertEqual(rect.to_dictionary(), {'x': 1, 'y': 9, 'id': 7, 'height': 2, 'width': 10})

    def test_update(self):
        rect = Rectangle(1, 2, 3, 4)
        rect.update(89, 2, 3, 4, 5)
        self.assertEqual(rect.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_create(self):
        dictionary = {"x": 1, "y": 0, "id": 1, "height": 3, "width": 5}
        rect = Rectangle.create(**dictionary)
        self.assertEqual(str(rect), "[Rectangle] (1) 1/0 - 5/3")

if __name__ == "__main__":
    unittest.main()

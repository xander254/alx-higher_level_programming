#!/usr/bin/python3
"""
Tests for the rectangle class
"""
from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangle(unittest.TestCase):
    """
    Tests for the rectangle class
    """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_multiple_initializations(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_with_all_values(self):
        r3 = Rectangle(10, 2, 7, 9, 12)
        self.assertEqual(r3.id, 12)

    def test_without_id(self):
        r4 = Rectangle(2, 4)
        self.assertEqual(r4.id, 3)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):
    """
    Test max integer
    """
    def test_with_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_one_element(self):
        self.assertEqual(max_integer([12]), 12)

    def test_with_negative(self):
        self.assertEqual(max_integer([-10, -6, -4, -11]), -4)

    def test_with_one_negative(self):
        self.assertEqual(max_integer([-10]), -10)

    def test_max_in_beg(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_max_at_middle(self):
        self.assertEqual(max_integer([1, 6, 4]), 6)

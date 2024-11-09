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

    def test_with_values(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

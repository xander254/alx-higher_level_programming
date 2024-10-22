#!/usr/bin/python3
from models.base import Base
"""
Unit tests for the Base Class.
"""
import unittest


class TestBase(unittest.TestCase):

    def test_init_without_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_init_with_id(self):
        b2 = Base(12)
        self.assertEqual(b2.id, 12)

    def test_multiple_instances(self):
        b3 = Base()
        b4 = Base()
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 3)

    def test_with_negative_id(self):
        b5 = Base(-30)
        self.assertEqual(b5.id, -30)

    def test_large_id(self):
        b6 = Base(9874983748437638273873263827628928676787)
        self.assertEqual(b6.id, 9874983748437638273873263827628928676787)

    def test_multiple_instances_with_id(self):
        b7 = Base(45)
        b8 = Base(36)
        self.assertEqual(b7.id, 45)
        self.assertEqual(b8.id, 36)


if __name__ == "__main__":
    unittest.main()

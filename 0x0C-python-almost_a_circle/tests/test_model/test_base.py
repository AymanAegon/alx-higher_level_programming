#!/usr/bin/python3
"""
test_base module
"""


import unittest
from models import base
Base = base.Base


class TestBase(unittest.TestCase):
    """
    Tests for models/base.py
    """
    def test_id(self):
        """test id is correct"""
        print(self.assertTrue(Base().id == "0"))
        self.assertTrue(Base(), self.id)
        self.assertTrue(Base(10), self.id)
        self.assertTrue(Base(), self.id)

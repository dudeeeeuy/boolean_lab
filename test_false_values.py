from unittest import TestCase
from false_values import *


class Test(TestCase):
    def test_false_boolean(self):
        self.assertEqual(bool(false_boolean()), False)

    def test_false_string(self):
        self.assertEqual(bool(false_string()), False)

    def test_false_int(self):
        self.assertEqual(bool(false_int()), False)

    def test_false_float(self):
        self.assertEqual(bool(false_float()), False)

from unittest import TestCase
from and_or import *


class Test(TestCase):
    def test_between_zero_and_one_true(self):
        self.assertEqual(between_zero_and_one(0.1), True)

    def test_between_zero_and_one_false(self):
        self.assertEqual(between_zero_and_one(1), False)

    def test_integer_or_float_integer_input(self):
        self.assertEqual(integer_or_float(5), True)

    def test_integer_or_float_float_input(self):
        self.assertEqual(integer_or_float(0.0), True)

    def test_integer_or_float_string_input(self):
        self.assertEqual(integer_or_float("77"), False)

    def test_integer_or_float_boolean_input(self):
        self.assertEqual(integer_or_float(True), False)
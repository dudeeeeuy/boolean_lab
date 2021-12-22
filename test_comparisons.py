from unittest import TestCase
from comparisons import *


class Test(TestCase):
    def test_greater_than_one(self):
        self.assertEqual(greater_than_one(), True)

    def test_you_are_number_one_alphabetically(self):
        self.assertEqual(you_are_number_one_alphabetically(), True)

    def test_are_you_voting_age(self):
        self.assertEqual(are_you_voting_age(), True)

    def test_were_not_so_different_you_and_i(self):
        self.assertEqual(were_not_so_different_you_and_i(), True)

    def test_we_are_not_the_same(self):
        self.assertEqual(we_are_not_the_same(), True)

import unittest
from classes.bar import Bar
from classes.drink import Drink
from classes.guest import Guest


class BarTest(unittest.TestCase):
    def setUp(self):
        self.bar = Bar(1000)
        self.drink = Drink("Old fashioned", 7)

    def test_bar_has_till(self):
        self.assertEqual(1000, self.bar.till)

    def test_bar_can_add_drinks(self):
        self.bar.add_drinks(self.drink,)
        self.assertEqual(1, len(self.bar.drinks))

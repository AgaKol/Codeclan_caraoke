import unittest
from classes.drink import Drink


class DrinkTest(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Daiquiri", 6)

    def test_drink_has_name(self):
        self.assertEqual("Daiquiri", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(6, self.drink.price)

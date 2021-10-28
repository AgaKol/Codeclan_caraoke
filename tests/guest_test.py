import unittest
from unittest.loader import defaultTestLoader
from classes.guest import Guest


class GuestTest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Harley Heptinstall", 50, 37,
                           "The Chauffeur", "Duran Duran")

    def test_guest_has_name(self):
        self.assertEqual("Harley Heptinstall", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest.wallet)

    def test_guest_has_age(self):
        self.assertEqual(37, self.guest.age)

    def test_guest_has_favourite_song(self):
        self.assertEqual("The Chauffeur", self.guest.favourite_song)

    def test_guest_has_favourite_artist(self):
        self.assertEqual("Duran Duran", self.guest.favourite_artist)

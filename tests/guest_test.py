import unittest
from unittest.loader import defaultTestLoader
from classes.guest import Guest
from classes.song import Song
from classes.drink import Drink
from classes.bar import Bar


class GuestTest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Harley Heptinstall", 50, 37,
                           "The Chauffeur", "Duran Duran")
        self.song = Song("The Chauffeur", "Deftones")
        self.song2 = Song("Planet Earth", "Duran Duran")
        self.song3 = Song("The Chauffeur", "Duran Duran")
        self.drink = Drink("Margarita", 5)
        self.bar = Bar(1000)

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

    def test_guest_cheer_favourite_song(self):
        self.assertEqual("Whoo!", self.guest.cheer(self.song))

    def test_guest_cheer_favourite_artist(self):
        self.assertEqual("Whoo!", self.guest.cheer(self.song2))

    def test_guest_cheer_favourite_song_and_artist(self):
        self.assertEqual("Whoo-hoo!", self.guest.cheer(self.song3))

    def test_guest_does_not_cheer(self):
        song = Song("Ines", "Boikot")
        self.assertEqual(None, self.guest.cheer(song))

    def test_guest_can_buy_drink(self):
        self.guest.buy_drink(self.drink, self.bar)
        self.assertEqual(1, len(self.guest.drinks_bought))
        self.assertEqual(45, self.guest.wallet)
        self.assertEqual(1005, self.bar.till)

    def test_guest_cannot_buy_drink(self):
        guest = Guest("Algernon Simonds", 4, 22, "Fashion", "David Bowie")
        self.assertEqual(None, guest.buy_drink(self.drink, self.bar))

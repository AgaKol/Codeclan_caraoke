import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class RoomTest(unittest.TestCase):
    def setUp(self):
        self.room = Room(15, 10)
        self.guest = Guest("Theobold Spencer", 100, 29,
                           "Bohemian Rhapsody", "Queen")
        self.guest2 = Guest("Prudence Robertson", 5, 17,
                            "Evil in your Eye", "Church of the Cosmic Skull")
        self.song = Song("Hell and You", "Amigo the Devil")

    def test_room_has_capacity(self):
        self.assertEqual(15, self.room.capacity)

    def test_room_has_entry_fee(self):
        self.assertEqual(10, self.room.entry_fee)

    def test_how_many_guests_in_room(self):
        self.assertEqual(0, len(self.room.guests_inside))

    def test_how_many_songs_added_to_room(self):
        self.assertEqual(0, len(self.room.songs))

    def test_guest_check_in(self):
        self.room.check_in(self.guest)
        self.assertEqual(1, len(self.room.guests_inside))
        self.assertEqual(90, self.guest.wallet)

    def test_guest_cannot_pay_entry_fee(self):
        message = "Sorry, you need to pay the fee before checking in."
        self.assertEqual(message, self.room.check_in(self.guest2))

    def test_guest_cannot_check_in_room_full(self):
        len(self.room.guests_inside) == 10
        message = "Sorry, the room is full. Please try another one."
        self.assertEqual(message, self.room.check_in(self.guest))

    def test_add_song(self):
        self.room.add_song(self.song)
        self.assertEqual(1, len(self.room.songs))

    def test_add_song_already_in_room(self):
        self.room.songs.append(self.song)
        message = "Song is already available in the room."
        self.assertEqual(message, self.room.add_song(self.song))

    def test_guest_check_out(self):
        self.room.check_in(self.guest)
        self.room.check_out(self.guest)
        self.assertEqual(0, len(self.room.guests_inside))

    def test_check_out_wrong_name(self):
        self.room.check_in(self.guest)
        message = "Sorry, name not recognised."
        self.assertEqual(message, self.room.check_out(self.guest2))

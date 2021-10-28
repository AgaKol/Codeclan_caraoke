import unittest
from classes.room import Room


class RoomTest(unittest.TestCase):
    def setUp(self):
        self.room = Room(15, 10)

    def test_room_has_capacity(self):
        self.assertEqual(15, self.room.capacity)

    def test_room_has_entry_fee(self):
        self.assertEqual(10, self.room.entry_fee)

    def test_room_is_empty(self):
        self.assertEqual(0, len(self.room.guests_inside))

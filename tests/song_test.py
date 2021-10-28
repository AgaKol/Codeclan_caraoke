import unittest
from classes.song import Song


class SongTest(unittest.TestCase):
    def setUp(self):
        self.song = Song("Like a Prayer", "Madonna")

    def test_song_has_name(self):
        self.assertEqual("Like a Prayer", self.song.title)

    def test_song_has_singer(self):
        self.assertEqual("Madonna", self.song.singer)

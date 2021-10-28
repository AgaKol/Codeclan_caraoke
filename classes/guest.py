class Guest:
    def __init__(self, name, wallet, age, favourite_song, favourite_artist):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.favourite_song = favourite_song
        self.favourite_artist = favourite_artist

    def cheer(self, song):
        if song.title == self.favourite_song and song.singer == self.favourite_artist:
            return "Whoo-hoo!"
        elif song.title == self.favourite_song or song.singer == self.favourite_artist:
            return "Whoo!"

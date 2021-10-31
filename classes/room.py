class Room:
    def __init__(self, capacity, entry_fee):
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.songs = []
        self.guests_inside = []

    def check_in(self, guest):
        if len(self.guests_inside) <= self.capacity and guest.wallet >= self.entry_fee:
            self.guests_inside.append(guest)
            guest.wallet -= self.entry_fee
        elif guest.wallet <= self.entry_fee:
            return "Sorry, you need to pay the fee before checking in."
        return "Sorry, the room is full. Please try another one."

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
        return "Song is already available in the room."

    def check_out(self, guest):
        if guest in self.guests_inside:
            self.guests_inside.remove(guest)
        return "Sorry, name not recognised."

    def check_guest_tab(self, guest):
        tab = self.entry_fee
        for drink in guest.drinks_bought:
            tab += drink.price
        return tab

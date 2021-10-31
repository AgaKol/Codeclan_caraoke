class Bar:
    def __init__(self, till):
        self.till = till
        self.drinks = []

    def add_drinks(self, drink):
        self.drinks.append(drink)

class Card:

    def __init__(self,suit,rank):
        # масть
        self.suit = suit
        # достоинство
        self.rank = rank

    def __str__(self):
        return f"{self.rank} {self.suit}"
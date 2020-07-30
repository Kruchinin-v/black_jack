from modules.global_vars import suits
from modules.global_vars import ranks
from modules.classes.Card import Card
import random

class Deck:

    def __init__(self):
        self.deck = []  # начинаем с пустого списка
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_full = ''
        for card in self.deck:
            deck_full += card.__str__() + '\n'
        return deck_full

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        x = random.randint(0,len(self.deck)-1)
        return self.deck.pop(x)


if __name__ == "__main__":
    try:
        theDeck = Deck()
        print(theDeck)
    except:
        print("error")
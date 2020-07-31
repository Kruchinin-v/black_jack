from modules.classes.Deck import Deck
from modules.classes.Chips import Chips
from modules.classes.Hand import Hand
from modules.functions.take_bet import take_bet
from modules.functions.show_some import show_some
from modules.functions.hit_or_stand import hit_or_stand
from modules.functions.progress import progress
from modules.functions.clear import clear
from modules.global_vars import playing
from modules.functions.hit import hit


while True:
    clear()

    print("Добро пожаловать в игру!")

    # создается колода карт
    theDeck = Deck()
    # перемешивается колода
    theDeck.shuffle()

    # определили количество фишек игрока
    theChips = Chips()

    # запросили ставку игрока
    bet = take_bet(theChips)

    print(f"Ставка {bet}$ принята")
    progress(4, 'Игра начнется через')

    print("Выдаем карты")

    # выдать игроку 2 карты
    handPlayer = Hand()
    hit(theDeck, handPlayer)
    hit(theDeck, handPlayer)

    # выдать компьюетру 2 карты
    handDealer = Hand()
    hit(theDeck, handDealer, 1)
    hit(theDeck, handDealer, 1)

    # вывести карты
    show_some(handPlayer, handDealer, bet, theChips.total)

    while playing:

        playing = hit_or_stand(theDeck, handPlayer)
        show_some(handPlayer, handDealer, bet, theChips.total)

    print("Дальше...")
    break

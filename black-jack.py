import os
from time import sleep

# подключение класса с колодой
from modules.classes.Deck import Deck

# подключение класса для подсчета фишек игрока
from modules.classes.Chips import Chips

# функция для запроса ставки игрока
from modules.functions.take_bet import take_bet

# подключение класса для хранения карт игрока
from modules.classes.Hand import Hand

# функция для отображения карт и прочей информации
from modules.functions.show_some import show_some

# функция, которая запрашивает действие игрока
from modules.functions.hit_or_stand import hit_or_stand

# функция прогресс-строка
from modules.global_vars import playing

# подключение
from modules.functions.progress import progress

while True:
    print("Добро пожаловать в игру!")

    # создается колода карт
    theDeck = Deck()
    # перемешивается колода
    theDeck.shuffle()

    # выдать игроку 2 карты
    handPlayer = Hand()
    handPlayer.add_card(theDeck.deal())
    handPlayer.add_card(theDeck.deal())

    # выдать компьюетру 2 карты
    handDealer = Hand()
    handDealer.add_card(theDeck.deal())
    handDealer.add_card(theDeck.deal())

    # определили количество фишек игрока
    theChips = Chips()

    # запросили ставку игрока
    bet = take_bet(theChips.total)

    print(f"Ставка {bet}$ принята")
    progress(4, 'Игра начнется через')

    # вывести карты
    show_some(handPlayer, handDealer, bet)

    while playing:

        hit_or_stand(theDeck,handPlayer)

        playing = 0
    break

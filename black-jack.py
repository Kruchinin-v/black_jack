import sys
from modules.classes.Deck import Deck
from modules.classes.Chips import Chips
from modules.classes.Hand import Hand
from modules.functions.take_bet import take_bet
from modules.functions.show_some import show_some
from modules.functions.hit_or_stand import hit_or_stand
from modules.functions.progress import progress
from modules.functions.clear import clear
from modules.functions.continue_the_game import continue_the_game
from modules.functions.hit import hit


def main():
    pass


game_on = True

try:
    balance = int(sys.argv[1])
except Exception:
    balance = 100

clear()
print("===================================================")
print("==========>> Игра Black-Jack by Ovod <<============")
print("===================================================")
print("")
print("Добро пожаловать в игру!")


while game_on:
    playing = True

    # создается колода карт
    theDeck = Deck()
    # перемешивается колода
    theDeck.shuffle()

    # определили количество фишек игрока
    theChips = Chips(balance)

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
    hit(theDeck, handDealer, mode=1)
    hit(theDeck, handDealer, mode=1)

    # вывести карты
    show_some(handPlayer, handDealer, bet, theChips.total)

    while playing:
        playing = hit_or_stand(theDeck, handPlayer)
        show_some(handPlayer, handDealer, bet, theChips.total)

    if handPlayer.value > 21:
        show_some(handPlayer, handDealer, bet, theChips.total, mode=1)
        print("Перебор")
        balance = theChips.total
        print(f"balance = {balance}")
        game_on = continue_the_game(balance)
        continue

    while handDealer.value < 17:
        hit(theDeck, handDealer, mode=1)

    show_some(handPlayer, handDealer, bet, theChips.total, mode=1)

    if handDealer.value > 21:
        print("У диллера перебор, Игрок выиграл! Поздравляю")
        balance += bet * 2
        print(f"balance = {balance}")
        game_on = continue_the_game(balance)
        continue
    elif handDealer.value < handPlayer.value:
        print("Игрок выиграл! Поздравляю")
        balance += bet * 2
        print(f"balance = {balance}")
        game_on = continue_the_game(balance)
        continue
    elif handDealer.value == handPlayer.value:
        print("Ничья")
        balance += bet
        print(f"balance = {balance}")
        game_on = continue_the_game(balance)
        continue
    else:
        print("Игрок приграл! Повезет в следующий раз")
        balance = theChips.total
        print(f"balance = {balance}")
        game_on = continue_the_game(balance)
        continue

    print("иной вариант???")
    game_on = continue_the_game(balance)

print("Игра окончена. Спасибо Вам за игру!")
print("Ждем Вас снова! Bay")


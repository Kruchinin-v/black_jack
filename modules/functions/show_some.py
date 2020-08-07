"""
Module for function show_some
"""
from modules.functions.clear import clear


def show_some(player, dealer, bet, balance, mode=0):
    """
    функция которая выводит карты игрока и 1 из 2х карт компьюетра

    :param player: объект руки игрока
    :type player: Hand
    :param dealer: объект руки диллера
    :type dealer: Hand
    :param bet: текущая ставка
    :type bet: int
    :param balance: баланс игрока
    :type bet: int
    :param mode: Промежуточный вывод - 0, вывод в конце игры - 1
    """

    clear()

    print("===================================================")
    print("==========>> Игра Black-Jack by Ovod <<============")
    print("===================================================")
    print("")

    print(f"Текущий баланс {balance}$")
    print(f"Текущая ставка {bet}$")

    print("Карты диллера:")
    if mode == 0:
        dealer.print_cards(1)
    else:
        dealer.print_cards(0)

    print("Ваши карты: ")
    player.print_cards(0)

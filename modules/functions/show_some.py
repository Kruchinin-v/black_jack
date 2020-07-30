"""
Module for function show_some
"""

import os


def show_some(player, dealer, bet):
    """
    функция которая выводит карты игрока и 1 из 2х карт компьюетра

    :param player: объект руки игрока
    :type player: Hand
    :param dealer: объект руки диллера
    :type dealer: Hand
    :param bet: текущая ставка
    :type bet: int
    """

    if os.name == 'nt':
        os.system("cls")
    elif os.name == 'posix':
        os.system("clear")

    print(f"Текущая ставка {bet}$")

    print("Карты диллера:")
    dealer.print_cards(1)

    print("Ваши карты: ")
    player.print_cards(0)

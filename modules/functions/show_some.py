"""
Module for function show_some
"""
from modules.functions.clear import clear


def show_some(player, dealer, bet, balance):
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
    """

    clear()
    print(f"Текущий баланс {balance}$")
    print(f"Текущая ставка {bet}$")

    print("Карты диллера:")
    dealer.print_cards(1)

    print("Ваши карты: ")
    player.print_cards(0)

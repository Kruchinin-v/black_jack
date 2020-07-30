"""
Module for function take_bet
"""


def take_bet(total):
    """
    функция, которая запрашивает у игрока ставку
    @:param total сколько всего валюты у игрока
    @:return bet принятая ставка
    """
    bet = 0
    while bet <= 0 or bet > total:
        try:
            bet = int(input(f"У вас сейчас {total}$. Ваша ставка: "))
            if bet > total:
                print("Нельзя установить ставку больше, чем у вас есть")
        except:
            print("не верное значение")
            bet = 0
    return bet

"""
Module for function take_bet
"""


def take_bet(theChips):
    """
    функция, которая запрашивает у игрока ставку
    @:param theChips сколько всего валюты у игрока
    @:return theChips принятая ставка
    """
    bet = 0
    balance = theChips.total
    while bet <= 0 or bet > balance:
        try:
            bet = int(input(f"У вас сейчас {balance}$. Ваша ставка: "))
            if bet > balance:
                print("Нельзя установить ставку больше, чем у вас есть")
        except KeyboardInterrupt:
            print("\nGood bye")
            raise SystemExit(0)
        except:
            print("неверное значение")
            bet = 0
    theChips.total -= bet
    return bet

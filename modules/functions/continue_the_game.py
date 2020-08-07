def continue_the_game(balance):
    """
    Спросить игрока, будем ли продолжать игру

    :param balance: текущий баланс игрока
    :return: 1 - продолжить игру, - закончить игру
    """
    if balance < 10:
        return 0

    next = input("Продолжим игру? (Y/N) ").lower()

    while next != 'y' and next != 'n':
        print("Не верный ввод, попробуем еще раз")
        next = input("Продолжим игру? (Y/N) ").lower()

    if next == 'y':
        return 1
    else:
        return 0

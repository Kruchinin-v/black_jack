def continue_the_game(balance):
    """
    Спросить игрока, будем ли продолжать игру

    :param balance: текущий баланс игрока
    :return: 1 - продолжить игру, 0 - закончить игру
    """
    if balance < 5:
        return 0

    next_ = input("Продолжим игру? (Y/N) ").lower()

    while next_ != 'y' and next != 'n':
        print("Не верный ввод, попробуем еще раз")
        next_ = input("Продолжим игру? (Y/N) ").lower()

    if next_ == 'y':
        return 1
    else:
        return 0

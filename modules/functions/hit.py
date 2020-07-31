from modules.functions.progress import progress


def hit(deck, hand, mode=0):
    """


    :param deck: колода
    :param hand: рука, куда добавить карту
    :param mode: указать 1, если выдавать карты диллеру
    """
    hand.add_card(deck.deal())

    count = 0

    if hand.value > 21 and hand.aces == 0:

        for i in hand.cards:
            if i.__str__().split(" ")[0] == "Туз":
                count += 1
    if count > 0:
        print(f"У вас {hand.value} очков, количество тузов - {count}")
        print("Меняем номинал тузов")
        hand.aces = 1
        hand.value -= 10 * count
        print(f"После замены у вас {hand.value} очков, еще можно поиграть:)")
        if mode == 0:
            progress(4, 'Игра продолжится через')

    return hand.value

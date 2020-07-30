def hit(deck, hand):
    """

    :param deck: колода
    :param hand: рука, куда добавить карту
    :return:
    """
    hand.add_card(deck.deal())

    if hand.value > 21 and hand.aces == 0:
        for i in hand.cards:
            if i.__str__().split(" ")[0] == "Туз":
                print("Есть шанс")
    return hand.value

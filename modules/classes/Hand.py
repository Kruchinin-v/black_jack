"""
Текст
"""

from modules.global_vars import values
from modules.functions.alignmebt_string import alignment_string


class Hand:
    """
    Рука
    """

    def __init__(self):
        self.cards = []  # начинаем с пустого списка
        self.value = 0  # начинаем со значения 0
        self.aces = 0  # добавляем атрибут, чтобы учитывать тузы

    def add_card(self, card):
        """
        Добавить карту в руку

        :param card: карта, которую необходимо добавить
        """
        self.cards.append(card)
        rank = self.cards[len(self.cards) - 1].__str__().split(' ')[0]
        self.value += values[rank]

    def adjust_for_ace(self):
        """
        Режим туза. True: туз стоит 11 очков. False - 1 очко
        """
        self.aces = not self.aces

    def print_cards(self, mode=0):
        """
        Выводит карты игрока на экран

        :param mode: показать все карты или только одну(для диллера в начале)
        0 - все карты
        1 - только одну

        """

        if mode == 0:
            count = len(self.cards)
        else:
            count = 1

        for i in range(count):
            card = self.cards[i].__str__()
            rank = card.split(" ")[0]
            card = alignment_string(f"{card} - {values[rank]}", 20)
            print("----------------------")
            print(f"| {card}|")
            print("----------------------")

        if mode == 0:
            print(f"Общая сумма: {self.value}")

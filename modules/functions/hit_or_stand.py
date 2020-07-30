# подключение переменной состояния игры
from modules.global_vars import playing

# подключение переменной состояния игры
from modules.functions.hit import hit
def hit_or_stand(deck, hand):

    more = input("Нужна еще карта? (Y/N) ").lower()
    while more != 'y' and more != 'n':
        print("Не верный ввод, попробуем еще раз")
        more = input("Нужна еще карта? (Y/N) ").lower()

    if more == 'y':
        value = hit(deck, hand)
        hand.print_cards(0)



import os


def clear():
    """
    Функция очищает экран
    """
    if os.name == 'nt':
        os.system("cls")
    elif os.name == 'posix':
        os.system("clear")

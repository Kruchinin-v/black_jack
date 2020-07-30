"""
Module for function alignment_string
"""


def alignment_string(string, length):
    """
    Функция для выравнивания строковой переменной до нужной длины
    с помощью пробелов


    :param string: входная переменная, которую нужно выровнять
    :type string: string
    :param length: необходимая длина переменной
    :type length: int

    :return string: строка, выровненная до указанной длины, с помощью пробелов
    :rtype string: string
    """

    while len(string) < length:
        string += " "
    return string

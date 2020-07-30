from time import sleep


def progress(count, suffix=''):
    """
    Функция для отображения отсчета времени
    :param count: сколько секунд отсчитывать
    :param suffix: какое сообщение писать
    """
    for i in range(count, 1, -1):
        print(f"\r{suffix} {i}", end="", flush=True)
        sleep(1)

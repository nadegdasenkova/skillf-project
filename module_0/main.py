import numpy as np


# функция угадывания
def game_core_v3(number):
    count = 0   # счетчик попыток
    _min = 1    # минимальное значение
    _max = 100  # максимальное значение
    _mid = int(_max / 2)  # середина диапазона по умолчанию

    # Если угадываемое число уже равно пороговым значениям, то нам повезло)
    if _min == number or _max == number:
        return 1

    while number != _mid:
        count += 1
        if number > _mid:
            _min = _mid
            _mid = int((_max + _mid) / 2)

        if number < _mid:
            _max = _mid
            _mid = int((_min + _mid) / 2)

    return count  # выход из цикла, если угадали


# функция тестирования
def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)  # генерация список из 1000 случайных чисел от 1 до 100
    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# тестирование
score_game(game_core_v3)

import numpy as np


def predict_random(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count =  0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)


def predict_half_sections(number:int=1) -> int:
    """Ищем загаданное число делением интервала пополам

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count =  0
    interval_min = 1
    interval_max = 100

    while True:
        count += 1
        predict_number = (interval_max + interval_min) // 2 # предполагаемое число
        
        if predict_number > number:
            interval_max = predict_number - 1
        elif predict_number < number:
            interval_min = predict_number + 1
        else:
            break

    return(count)


def predict_random_v2(number:int=1) -> int:
    """Ищем загаданное число генерируя случайные числа в сужающемся интервале

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count =  0
    interval_min = 1
    interval_max = 100

    while True:
        count += 1
        predict_number = np.random.randint(interval_min, interval_max + 1) # предполагаемое число
        
        if predict_number > number:
           interval_max = predict_number - 1
        elif predict_number < number:
            interval_min = predict_number + 1
        else:
            break # выход из цикла, если угадали
        
    return(count)


def score_calc(*args) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    scores = dict() #словарь для хранения результата каждого алгоритма угадывания
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for predict_func in args:

        count_ls = [] # обнуляем список для сохранения количества попыток

        for number in random_array:
            count_ls.append(predict_func(number))

        scores[predict_func.__name__] = int(np.mean(count_ls)) # находим среднее количество попыток
        print(f'Алгоритм "{predict_func.__name__}" угадывает число в среднем за {scores[predict_func.__name__]} попыток')

    return(scores)


if __name__ == '__main__':
    print(score_calc(predict_random, predict_half_sections, predict_random_v2))
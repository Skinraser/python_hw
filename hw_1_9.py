# Нормировать одномерный список случайных чисел. Нормирование означает приведение всех значений массива к
# интервалу [-1;1], причем максимальное абсолютное значение элементов после нормирование должно быть равно 1.
# Например, последовательность [-5, 3, 4] после нормирование будет выглядеть [-1, 0.6, 0.8]
import random
lst = [random.randint(-5, 5) for i in range(10)]
lst1 = []


def normalize_lst(list):
    for elem in lst:
        elem = elem / abs(max(lst, key=lambda elem : abs(elem)))
        lst1.append(elem)
    return lst, lst1


print(normalize_lst(lst))

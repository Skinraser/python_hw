import random
lst = []


def calc_frequency(lst): # returns the most frequent number or None
    for i in range(11):
        lst.append(random.randint(-1, 1))
        print(lst)
    if (lst.count(1) > lst.count(-1)) and (lst.count(1) > lst.count(0)):
        print('Цифра 1 встречается больше раз чем -1 и 0')
        return lst.count(1)
    elif (lst.count(-1) > lst.count(1)) and (lst.count(-1) > lst.count(0)):
        print('Цифра -1 встречается больше раз чем 1 и 0')
        return lst.count(-1)
    elif (lst.count(0) > lst.count(1)) and (lst.count(0) > lst.count(-1)):
        print('Цифра 0 встречается больше раз чем 1 и -1')
        return lst.count(0)
    elif (lst.count(0) == lst.count(1)) or (lst.count(0) == lst.count(-1)) or (lst.count(-1) == lst.count(1)):
        print('Два значения повторяются одинаковое количество раз')
        return None


print(calc_frequency(lst))

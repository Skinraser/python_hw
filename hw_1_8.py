# В одномерном списке поменять местами минимальный и максимальный элементы. Остальные оставить на своих местах.
lst = [i for i in range(10)]


def change_min_and_max(lst):
    lst.insert(max(lst), min(lst))
    lst.insert(min(lst), max(lst))
    lst.remove(min(lst))
    lst.reverse()
    lst.remove(max(lst))
    lst.reverse()
    return lst


print(change_min_and_max(lst))

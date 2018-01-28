# В одномерном списке поменять местами минимальный и максимальный элементы. Остальные оставить на своих местах.
lst = [2, 1, 3, 8]


def change_min_and_max(lst):
    maximum = lst.index(max(lst))
    minimum = lst.index(min(lst))
    lst[maximum], lst[minimum] = lst[minimum], lst[maximum]
    return lst


print(change_min_and_max(lst))

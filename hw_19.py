import random


def diff_min_max(num_limit, lower_bound, upper_bound): # returns int
    lst = []
    for i in range(num_limit):
        lst.append(random.randint(lower_bound, upper_bound))
    max_value = max(lst)
    min_value = min(lst)
    difference = max_value - min_value
    print('Max value: %d, Min value: %d, Difference: %d' % (max_value, min_value, difference))


diff_min_max(5, 10, 100)

import random
def get_max_digit(number): # returns int
    lst = []
    for i in str(number):
        lst.append(i)
    max_value = max(lst)
    print(lst)
    return max_value


print(get_max_digit(random.randint(100000000000, 999999999999)))
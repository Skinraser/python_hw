import random
def diff_even_odd(num_limit, lower_bound, upper_bound): # returns int
    total_even = 0
    total_odd = 0
    for i in range(num_limit):
        number = random.randint(lower_bound, upper_bound)
        if number % 2 == 0:
            total_even += number
        elif number % 2 == 1:
            total_odd += number
    difference = total_even - total_odd
    return difference


print(diff_even_odd(50, 5, 50))

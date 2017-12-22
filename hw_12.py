def sum_of_digits(number):
    n1 = number % 10
    number = number // 10
    n2 = number % 10
    number = number // 10
    n3 = number % 10
    number1 = n1 + n2 + n3
    return number1


number2 = sum_of_digits(555)
print("Сумма цифр числа:", number2)

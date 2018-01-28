# Создать программу, выводящую на экран ближайшее к 10 из двух чисел, введенных пользователем. Например, среди чисел 8,5 и 11,45 ближайшее к десяти 11,45.


def closer_to_ten(number1, number2):
    delta1 = abs(10 - number1)
    delta2 = abs(10 - number2)
    if delta1 < delta2:
        return 'Число %d ближе к 10 чем число %d' % (number1, number2)
    elif delta2 < delta1:
        return 'Число %d ближе к 10 чем число %d' % (number2, number1)
    elif delta2 == delta1:
        return 'Число %d и %d находятся на одинаковом расстоянии от 10' % (number2, number1)


print(closer_to_ten(int(input()), int(input())))

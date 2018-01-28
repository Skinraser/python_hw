# 1Найти произведение нечетных цифр пятизначного целого числа, введенного пользователем с клавиатуры


def multiple_of_uneven(number):
    result = 1
    for i in number:
        if int(i) % 2 == 1:
            result *= int(i)
    return result


print(multiple_of_uneven(input()))

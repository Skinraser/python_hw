import random
number = random.randint(1, 10)
player_number = 0
print('Программа загадала случайное число в диапазоне от 1 до 10, угадайте его.')
while player_number != number:
    print('Введите число:')
    player_number = int(input())
    if player_number == number:
        print('Вы угадали число! Поздравляю!')
        break
    elif player_number > number:
        print('Введеное число больше загадонного, попробуйте еще раз')
        continue
    elif player_number < number:
        print('Введеное число меньше загадонного, попробуйте еще раз')
        continue

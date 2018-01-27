# 7. Найти сумму десяти первых чисел ряда Фибоначчи


def fibonacci(n=10):
        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci())

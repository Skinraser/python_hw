import math


def triangle_square_and_perimeter(a, b):
    triangle_square = (1/2)*a*b
    c = math.sqrt(b**2 + a**2)
    triangle_perimeter = a + b + c
    return triangle_perimeter, triangle_square


square_and_perimeter = triangle_square_and_perimeter(5, 6)
square = square_and_perimeter[0]
print('Площадь и периметр равны %.2f и %.2f' % square_and_perimeter)

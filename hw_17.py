import math


def solve_quadratic_equation(a, b, c): # returns 2 values: either 2 roots or 2 Nones
    Discriminant = b**2 - 4 * a * c
    if Discriminant > 0:
        x1 = (-b + math.sqrt(Discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(Discriminant)) / (2 * a)
        return x1, x2
    elif Discriminant == 0:
        x1 = -b / (2 * a)
        x2 = None
        return x1, x2
    else:
        x1 = None
        x2 = None
        return x1, x2

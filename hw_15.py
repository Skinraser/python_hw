import math


def circles_intersects(x1, y1, r1, x2, y2, r2):
    r = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    return r1 + r2 >= r and r1 + r >= r2 and r2 + r >= r1


print(circles_intersects(5, 10, 1, 10, 5, 10))

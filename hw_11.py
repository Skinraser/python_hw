import math


def degrees2radians(degrees): # returns float
    radians = math.radians(degrees)
    return radians


cos60 = math.cos(degrees2radians(60))
cos45 = math.cos(degrees2radians(45))
cos30 = math.cos(degrees2radians(30))
print('Косинус 60 = %.2f , косинус 45 = %.2f , косинус 30 = %.2f ' % (cos60, cos45, cos30))

# ch05_03.py
# overriding

import math


class shape:
    def __init__(self):
        print('call __init__ from shape class')

    def calculate_area(self):
        print('calling calculate_area() from shape class')
        return 0


class circle(shape):
    def __init__(self, r):
        print('call __init__ from circle class')
        self.r = r

    def calculate_area(self):
        print('calling calculate_area() from circle class')
        return math.pi * self.r * self.r


class rectangle(shape):
    def __init__(self, l, w):
        print('call __init__ from rectangle class')
        self.l = l
        self.w = w

    def calculate_area(self):
        print('calling calculate_area() from rectangle class')
        return self.l * self.w


a = shape()
area = a.calculate_area()
print('area:', area)

b = circle(5)
area = b.calculate_area()
print('area:', area)

c = rectangle(2, 3)
area = c.calculate_area()
print('area:', area)

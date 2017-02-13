# ch05_02.py
# inheritance

import math


class shape:
    def __init__(self):
        print('call __init__ from shape class')

    def foo(self):
        print('calling foo() from shape class')


class circle(shape):
    def __init__(self, r):
        print('call __init__ from circle class')
        self.r = r

    def calculate_area_circle(self):
        return math.pi * self.r * self.r


class rectangle(shape):
    def __init__(self, l, w):
        print('call __init__ from rectangle class')
        self.l = l
        self.w = w

    def calculate_area_rectangle(self):
        return self.l * self.w


a = shape()
a.foo()

b = circle(5)
b.foo()
area = b.calculate_area_circle()
print('area:', area)

c = rectangle(2, 3)
c.foo()
area = c.calculate_area_rectangle()
print('area:', area)

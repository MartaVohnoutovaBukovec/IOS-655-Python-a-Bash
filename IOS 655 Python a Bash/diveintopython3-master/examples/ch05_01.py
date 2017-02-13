# ch05_01.py
# classes

from math import *


class City:
    # class data
    city_count = 0
    city_id = 0

    # constructor
    def __init__(self, name='', x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
        City.city_count += 1  # access all City classes
        self.city_id = City.city_count

    def __str__(self):
        return 'City: ' + self.name + ',id=' + str(self.city_id) + ',x=' + str(self.x) + ',y=' + str(self.y)

    # class attributes
    def move_to(self, x=0, y=0):
        self.x += x
        self.y += y

    def distance(self, other_city):
        xi = pow(other_city.x - self.x, 2)
        yi = pow(other_city.y - self.y, 2)

        return sqrt(xi + yi)

    def __del__(self):
        # get class name
        class_name = self.__class__.__name__
        print('class ', class_name, ' destroyed')


a = City('Hamburg', 10, 5)
b = City('Berlin', 3, 10)
print(a)
print(b)
print(City.city_count)


a.move_to(4, 3)
b.move_to(7, 12)
print(a)
print(b)

distance = a.distance(b)
print(distance)


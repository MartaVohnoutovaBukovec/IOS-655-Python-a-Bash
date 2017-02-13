# ch05_04.py
# overloading operator


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __str__(self):
        return 'x' + str(self.x) + ', y:' + str(self.y)


a = Point(10, 3)
b = Point(2, 7)
c = Point(8, 1)

print(a)
print(a + b)
print(c - b)
print(a * c)



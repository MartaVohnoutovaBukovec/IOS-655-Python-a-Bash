# ch03_02.py
# tuples - immutable (unchangeable) sequences of object


# declare tuples
a = ()
b = (3, 5, 7)
c = ('Ford', 'BMW', 'Toyota')
d = (3, (5, 'London'), 12)

# print
print(a)
print(b)
print(c)
print(d)

# get length of tuples
print(len(a))
print(len(b))
print(len(c))
print(len(d))


# get item
print(b[2])
print(c[1])

# get index
print(b.index(7))
print(c.index('Toyota'))


# ch03_01.py
# lists

# declare lists
print('----declare lists')
numbers = []
a = [2, 7, 10, 8]
cities = ['Berlin', 'Seattle', 'Tokyo', 'Moscow']
b = [10, 3, 'Apple', 6, 'Strawberry']
c = range(1, 10, 2)

# print(lists
print('----print(lists')
print(a)
for city in cities:
    print(city)

print(b)
print(c)

# get length of lists
print('----get length of lists')
print(len(a))
print(len(cities))

# add item into list
print('----add item')
numbers.append(10)
numbers.append(5)
cities.append('London')

for i in numbers:
    print(i)

for city in cities:
    print(city)


# get specific item
print('----get item')
print(cities[2])
print(a[3])


# sorting
print(a.sort())

# edit item
print('----edit item')
cities[2] = 'new city'
for city in cities:
    print(city)


# remove item
print('----remove item')
a.remove(8)   # by value
del cities[2]   # by index
for city in cities:
    print(city)


# ch07_01.py
# string operations


str1 = "hello world"
str2 = "python"

# Concatenating
print(str1 + " " + str2)
print(str1, str2)
print("%s %s" % (str1, str2))
print("{} {}".format(str1, str2))


# string to numeric
a = "2"
b = "6.8"

num1 = int(a)
num2 = float(b)
print(num1)
print(num2)


# numeric to string
a = 6
b = 8.56

str1 = str(a)
str2 = str(b)
print(str1)
print(str2)


# parsing
msg = 'Berlin;Amsterdam;London;Tokyo'
cities = msg.split(';')
for city in cities:
    print(city)


# string operations
msg = 'Hello world, Python!'

# upper & lower
print(msg.upper())
print(msg.lower())

# copy
print(msg[5:])
print(msg[:5])
print(msg[-3:])
print(msg[:-3])
print(msg[2:6])
print(msg[5:8])

# get a length of string
length = len(msg)
print(length)


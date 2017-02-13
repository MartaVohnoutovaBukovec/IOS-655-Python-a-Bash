# ch02_06.py

# comparison operators
a = 3
b = 8

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)


# logical operators

print((a == b) and (a != b))
print((a <= b) or (a > b))
print(not (a >= b))


# bitwise operators
# declare binary variables
m = 0b01010011
n = 0b11111001

print(m)
print(n)
print(bin(m & n))
print(bin(m | n))
print(bin(m ^ n))
print(bin(~m))
print(bin(b << 3))
print(bin(b >> 2))


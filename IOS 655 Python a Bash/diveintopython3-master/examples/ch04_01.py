# ch04_01.py
# functions


def foo():
    print('foo()')


def calculate(val_a, val_b):
    val = val_a * val_b
    return val


def perform(num):
    d = num * 5
    return d, d + 5, d - 2


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


foo()
m = calculate(10, 5)
print(m)
a, b, c = perform(5)
print(a)
print(b)
print(c)
res = fibonacci(10)
print(res)


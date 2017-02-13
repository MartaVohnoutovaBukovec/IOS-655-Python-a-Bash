# ch09_02.py
# handling error

# handle a zero division error

try:
    a = 18
    b = 0

    c = a / b
    print('result:', str(c))

except ZeroDivisionError as e:
    print('Error: division by zero')
    print(e)

finally:
    print('Done')

print('exit from program')

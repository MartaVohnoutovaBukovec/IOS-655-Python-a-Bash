# ch09_03.py
# handling error


# catch all errors

try:
    a = 18
    b = 0

    c = a / b
    print('result:', str(c))

except Exception as e:
    print(e)

finally:
    print('Done')

print('exit from program')

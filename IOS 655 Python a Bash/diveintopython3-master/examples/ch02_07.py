# ch02_07.py
# decision control

# if-else
a = 10
b = 30

print('demo if-elif-else')
if (a > 10) or (b > 10):
    # do something
    print('(a > 10) or (b > 10)')

elif (a != 5) and (b <= 7):
    # do something
    print('(a != 5) and (b <= 7)')

else:
    # do something
    print('else')


# nested if
if (a == 0) or (b > 20):
    if b < 50:
        print('nested-if')
    else:
        print('else-nested-if')
else:
    print('if-else')


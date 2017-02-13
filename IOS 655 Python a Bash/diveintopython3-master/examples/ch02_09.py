# ch02_09.py
# break, continue and pass

print('demo - break, continue and pass')
for i in range(1, 10):
    if i == 4:
        continue

    if i == 7:
        break
    print(i)


pass  # do nothing
print('This is the end of program')

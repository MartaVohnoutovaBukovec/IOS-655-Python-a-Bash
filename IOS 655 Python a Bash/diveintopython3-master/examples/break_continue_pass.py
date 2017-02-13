# break continue pass

print("break")
for i in range(0,10):
    if i == 6:
        break
    print(i)

print("continue")
for i in range(0,10):
    if i == 6:
        print("here")
        continue
    print(i)

print("pass")
for i in range(0,10):
    if i == 6:
        print("here")
        pass
    print(i)

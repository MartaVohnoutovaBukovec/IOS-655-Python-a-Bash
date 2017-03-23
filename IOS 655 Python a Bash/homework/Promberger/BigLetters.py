zero = ["  00  "," 0  0 ", "0    0", "0    0", "0    0", " 0  0 ", "  00  "]
one = [" 1 ", "11 ", " 1 ", " 1 ", " 1 ", " 1 ", "111"]
two = [" 222 ", "2   2", "   2 ", "  2  ", " 2   ", "2    ", "22222"]
three = [" 333 ", "3   3", "    3", "  33 ", "    3", "3   3", " 333 "]
four = ["   4  ", "  44  ", " 4 4  ", "4  4  ", "444444", "   4  ","   4  "]
five = ["55555", "5    ", "5    ", " 555 ", "    5", "5   5", " 555 "]
six = [" 666 ", "6    ", "6    ", "6666 ", "6   6", "6   6", " 666 "]
seven = ["77777", "    7", "   7 ", "  7  ", " 7   ", "7    "]
eight = [" 888 ", "8   8", "8   8", " 888 ", "8   8", "8   8", " 888 "]
nine = [" 999", "9   9", "9   9", " 9999", "    9", "    9", "  999"]
inpt=input("Enter a number:")
for num in inpt:
    if int(num)== 0:
        for i in zero:
            print(i)
    if int(num)== 1:
        for i in one:
            print(i)
    if int(num)== 2:
        for i in two:
            print(i)
    if int(num)== 3:
        for i in three:
            print(i)
    if int(num)== 4:
        for i in four:
            print(i)
    if int(num)== 5:
        for i in five:
            print(i)
    if int(num)== 6:
        for i in six:
            print(i)
    if int(num)== 7:
        for i in seven:
            print(i)
    if int(num)== 8:
        for i in eight:
            print(i)
    if int(num)== 9:
        for i in nine:
            print(i)


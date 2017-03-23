zero = ["  00  "," 0  0 ", "0    0", "0    0", "0    0", " 0  0 ", "  00  "]
one = [" 1 ", "11 ", " 1 ", " 1 ", " 1 ", " 1 ", "111"]
two = [" 222 ", "2   2", "   2 ", "  2  ", " 2   ", "2    ", "22222"]
three = [" 333 ", "3   3", "    3", "  33 ", "    3", "3   3", " 333 "]
four = ["   4  ", "  44  ", " 4 4  ", "4  4  ", "444444", "   4  ","   4  "]
five = ["55555", "5    ", "5    ", " 555 ", "    5", "5   5", " 555 "]
six = [" 666 ", "6    ", "6    ", "6666 ", "6   6", "6   6", " 666 "]
seven = ["7777777", "     7", "    7 ", "   7  ", "  7   ", " 7    ","7     "]
eight = [" 888 ", "8   8", "8   8", " 888 ", "8   8", "8   8", " 888 "]
nine = [" 999", "9   9", "9   9", " 9999", "    9", "    9", "  999"]
inpt=input("Enter a number:")
wholeNumber=[""]*7
for num in inpt:
    
    if int(num)== 0:
        for i in range(0,7):
            addStr=zero[i]+"  "
            wholeNumber[i]+=addStr
    if int(num)== 1:
        for i in range(0,7):
            addStr=one[i]+"  "
            wholeNumber[i]+=addStr
    if int(num)== 2:
        for i in range(0,7):
            addStr=two[i]+"  "
            wholeNumber[i]+=addStr
    if int(num)== 3:
        for i in range(0,7):
            addStr=three[i]+"  "
            wholeNumber[i]+=addStr
    if int(num)== 4:
        for i in range(0,7):
            addStr=four[i]+"  "
            wholeNumber[i]+=addStr
    if int(num)== 5:
        for i in range(0,7):
            addStr=five[i]+"  "
            wholeNumber[i]+=addStr
    if int(num)== 6:
        for i in range(0,7):
            addStr=six[i]+"  "
            wholeNumber[i]+=addStr
    if int(num)== 7:
        for i in range(0,7):
            addStr=seven[i]+"  "
            wholeNumber[i]+=addStr
    if int(num)== 8:
        for i in range(0,7):
            addStr=eight[i]+"  "
            wholeNumber[i]+=addStr
    if int(num)== 9:
        for i in range(0,7):
            addStr=nine[i]+"  "
            wholeNumber[i]+=addStr
for i in wholeNumber:
    print(i)


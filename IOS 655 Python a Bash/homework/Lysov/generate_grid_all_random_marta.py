#!/usr/bin/env python3
# all randoms Marta
import random

rows=random.randint(5, 30)
columns=random.randint(2, 15)
row,column=0,0

while row < rows:
    line = ""
    column = 0
    while column < columns:
        i = random.randint(-200,200)
        s = str(i)
        while len(s) < 10:
            s = " " + s
        line += s
        column += 1
    print(line)
    row += 1

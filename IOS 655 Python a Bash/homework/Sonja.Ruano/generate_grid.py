#!/usr/bin/env python3

import random

rows=int(input("Enter a number of rows: "))
columns=int(input("Enter a number of columns: "))

row = 0
while row < rows:
    line = ""
    column = 0
    while column < columns:
        i = random.randint(0, 1000)
        s = str(i)
        while len(s) < 10:
            s = " " + s
        line += s
        column += 1
    print(line)
    row += 1
    
#I am not sure I understand the function of each line.
    

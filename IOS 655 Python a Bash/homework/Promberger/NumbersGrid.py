import random
rows=random.randint(10,15)
colums=random.randint(10,15)
def createBox(number):
    box=["___", "|   ", "| ",number," ","|"]
    return box

for row in range(0,rows):
    rowtop=list()
    rowSecond=list()
    for colum in range(0,colums):
        rowtop.append("----")
        a=random.randint(-99,9)
        addSecond=["| ", a, " "]
        rowSecond.append(addSecond)
    
    for i in rowtop:
        print(i, end='')
    print("\n")
    for i in rowSecond:
        for k in i:
            print(k, end='')
    print("|\n")

import random

def	getRandomInt(minimum,maximum):
	return random.randint(minimum, maximum)

def drawLine(Length):
	for c in range(0,Length):
		print("+-",end="")
	print("+")

def drawCol():
	print("|" + str(getRandomInt(-9999,9999)),end="")
	
def drawGrid(rowCount, colCount):
	print()
	for r in range(0,rowCount):
		drawLine(colCount)
		for c in range(0,colCount):
			drawCol()
		print("|")
	drawLine(colCount)
	print()
	
minimum = 1
maximum = 10

print("The Grid will have dimensions between " + str(minimum) + " and " + str(maximum))
print("It will be filled with digits")

while True:
	rC = getRandomInt(minimum,maximum)
	cC = getRandomInt(minimum,maximum)
	print("Rowcount: " + str(rC) + " Colcount: " + str(cC))
	drawGrid(rC,cC)
	input("Press enter for the next Grid...")

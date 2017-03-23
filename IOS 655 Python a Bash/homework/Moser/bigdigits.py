def	getInt():
	while True:
		try:
			i = int(input("Please enter a positive Integer: "))
			if i < 0:
				continue
			print()
			return i
		except ValueError as err:
			print(err)

Zero = ["  ***  "," *   * ","*     *","*     *","*     *"," *   * ","  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ","   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

digitAsciiLength = 7

while True:
	number = str(getInt())
	for	row in range(0,digitAsciiLength):
		for i in range(0,len(number)):
			digitsIndex = int(number[i])
			print(Digits[digitsIndex][row], end=" ")
		print()
	print()
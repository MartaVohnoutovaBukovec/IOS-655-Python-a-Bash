def reverseStr(str):
	return str[::-1]

def	base2base(number, origBase, newBase):
	intValue = int(number,origBase)
	if(intValue == 0):
		return "0"
	rest = 0
	newValue = ""
	negative = False
	if(intValue < 0):
		intValue *= (-1)
		negative = True
	while intValue != 0:
		rest = intValue % newBase
		intValue = intValue//newBase
		if(rest >= 10):
			newValue += chr(ord('a') + rest - 10)
		else:
			newValue += str(rest)
	if(negative):
		newValue += "-"
	return reverseStr(newValue)

print(base2base("vlcice",36,2))

def decryptLetter(letter, keyLetter):
	if(letter.islower()):
		intValueA = ord('a')
		intValueZ = ord('z')
		keyLetter = keyLetter.lower()
	else:
		intValueA = ord('A')
		intValueZ = ord('Z')
		keyLetter = keyLetter.upper()
	intValue = ord(letter) - ord(keyLetter) + intValueA
	if(intValue < intValueA):
		intValue += (intValueZ - intValueA + 1)
	return chr(intValue)

def encryptLetter(letter, keyLetter):
	if(letter.islower()):
		intValueA = ord('a')
		intValueZ = ord('z')
		keyLetter = keyLetter.lower()
	else:
		intValueA = ord('A')
		intValueZ = ord('Z')
		keyLetter = keyLetter.upper()
	intValue = ord(letter) + ord(keyLetter) - intValueA
	if(intValue > intValueZ):
		intValue -= (intValueZ - intValueA + 1)
	return chr(intValue)

def	vigenere(message, key, encrypt):
	newMessage = ""
	newLetter = " "
	for i in range(len(message)):
		keyIndex = i%len(key)
		if(message[i] != " "):
			if(encrypt):
				newLetter = encryptLetter(message[i],key[keyIndex])
			else:
				newLetter = decryptLetter(message[i],key[keyIndex])
		else:
			newLetter = " "
		print(message[i], key[keyIndex], newLetter)
		newMessage += newLetter
	return newMessage
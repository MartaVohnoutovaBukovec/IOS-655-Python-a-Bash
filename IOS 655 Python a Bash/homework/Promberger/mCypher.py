# Module mCipher
# Vigere cipher function

def vigenere(strin,key,en):
    strin = strin.replace(" ","").upper()  
    key = key.replace(" ","").upper()
    sout=""
    if (len(strin)>len(key)):
        iterations = ((len(strin)-len(key))//len(key))+1
        keynew = key
        for i in range(iterations):
            keynew += key
    else:
        keynew = key
    if en:            
        for i in range(len(strin)):
            number=ord(strin[i])+ord(keynew[i])-65
            if (number>90):
                number -= 26
            sout += chr(number)
        print(sout)
    else:
        for i in range(len(strin)):
            number=ord(strin[i])-ord(keynew[i])+65
            if (number<65):
                number += 26
            sout += chr(number)
        print(sout)
    return sout


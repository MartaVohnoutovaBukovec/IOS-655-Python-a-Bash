# Module mCipher
# Vigerere cipher function

def vigenere(s,k,en):
        
    s,k=s.replace(" ","").upper(),k.replace(" ","").upper()     # remove all spaces and chenge to all capitals - for string and key
    out_s = ""
    
    if len(s) > len(k):
        k = (k * len(s))[0:len(s)]                              # add key to the length of string 
    else:
        k = k[:len(s)]

    if en:       
        for i in range(len(s)):
            if ord(s[i]) in range(65,91):                       # outside alphabets let it be as it is
                number_ord = ord(s[i]) + ord(k[i]) - 65
                if number_ord > 90:                             # adjust alphabet boundary
                    number_ord -= 26
            else:
                number_ord = ord(s[i])
            
            out_s = out_s + chr(number_ord)
    else:
        for i in range(len(s)):
            if ord(s[i]) in range(65,91):                       # outside alphabets let it be as it is
                number_ord = ord(s[i]) - ord(k[i]) + 65
                if number_ord < 65:                             # adjust alphabet boundary
                    number_ord += 26
            else:
                number_ord = ord(s[i])
                
            out_s = out_s + chr(number_ord)
   
    return  out_s

#print(vigenere("kleinehaarschnittkoch","brinellrockwellvickers",1))
#print(vigenere("LCMVRPSROTCYLYTOBMYGY","brinellrockwellvickers",0))

#print(vigenere("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz","brinellrockwellvickers",1))
#print(vigenere("AQHMDKKQNBJVDKKUHBJDQRAQHMDKKQNB","brinellrockwellvickers",0))

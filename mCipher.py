# Module mCipher
# Vigerere cipher function
# Caesar cipher function
# Affine cipher
# Vernam cipher

import math as m
from operator import itemgetter, attrgetter

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
  
def caesar_cipher(s,move,en):
    s_en = ""
    s_i = ""
    if not en:
        for i in s.upper():
            if ord(i) in range(65,91):
                j = ord(i) + move
                if j not in range(65,90):
                    j -= 26
            else:
                j = ord(i)
                
            s_en += chr(j)
    else:
        for i in s.upper():
            if ord(i) in range(65,91):
                j = ord(i) - move
                if j not in range(65,90):
                    j += 26
            else:
                j = ord(i)
                
            s_en += chr(j)

    return s_en


def getKey(item):
	return item[1]

def trans_cipher(string,keyword,en):

    k = list(enumerate(keyword.upper()))    
    k = sorted(k, key=itemgetter(1))
    keys = [(i,k[i][0]) for i in range(len(k))]
    string_en=""

    if en:           
        for i in range(0,len(string),len(keys)):
            for j in keys:
                try:
                    string_en += string[i+j[1]]
                except IndexError:
                    pass
    else:
      
        keys = sorted(keys,key=getKey)        
        for i in range(0,len(string),len(keys)):
            for j in keys:
                try:
                    string_en += string[i+j[0]]
                except IndexError:
                    pass       
    
    return string_en                           


def affine_cipher(string,en):

    s_en=""
    
    if en:
        try:
            for i in string:
                if i.isalpha():
                    s_en += chr((5*(ord(i.upper()) - 65) + 8) % 26 + 65).upper()
                else:
                    s_en += i
                    
        except IndexError:
            pass
    else:
        try:
            for i in string:
                if i.isalpha():
                    s_en += chr(21*((ord(i.upper()) - 65) - 8) % 26 + 65).upper()
                else:
                    s_en += i
                    
        except IndexError:
            pass

    return s_en

# Vernam cypher demo
# T Street 2015-10-16

def makeVernamCypher( text, key ):
    """ Returns the Vernam Cypher for given string and key """
    answer = "" # the Cypher text
    p = 0 # pointer for the key
    for char in text:
        answer += chr(ord(char) ^ ord(key[p]))
        # print(ord(char) ^ ord(key[p]))
        p += 1
        if p==len(key):
            p = 0
    return answer

                      


# mCipher.trans_cipher("I have a cat her name is Tit and on the mat she loves to sit","Python",1)
# mCipher.vigenere("I have a cat her name is Tit and on the mat she loves to sit","python",1)
# mCipher.caesar_cipher("I have a cat her name is Tit and on the mat she loves to sit",13,1)

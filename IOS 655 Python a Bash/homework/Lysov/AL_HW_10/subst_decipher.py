#!/usr/bin/env python3
#
# Subject: UAI / 655, Lecturer Ing. Marta Vohnoutová
# Homework No 10: create a program that breaks the substitution cipher
# using 'brute force' approach by seeking patterns in the English dictionary
#
# Author: Alexandre Lysov
# Date: April 2017
#
# on Linux: python3 subst_decipher.py < emsg.txt
# on Windows: python subst_decipher.py < emsg.txt
#
# Note: all files were creaed in Windows !
# If database cannot be opened, try to delete the en_dict.db file -
# the program will attempt to recreate it from en_words.txt file.
# Be aware of possible issues with line endings between Linux and Windows.

from enDict import enDict

def main():
    
    en_dict = enDict() 
    if (en_dict.access("en_dict.db") != 0):
        print("Cannot open dictionary.")
        return 1

    eMsg = ""
    line = ""
    while True:
        try:
            line = input(">")
            if line:
                eMsg += line.strip() + ' '
            else:
                break
        except EOFError:
            break

    eMsg = eMsg.strip()

    if (len(eMsg) > 0):
        print("Encrypted message:")
        print(eMsg)    

        dMsg = en_dict.decipher(eMsg)
        print(dMsg)

    return 0

main()

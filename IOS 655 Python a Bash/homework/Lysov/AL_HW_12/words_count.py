#!/usr/bin/env python3
#
# Subject: UAI / 655, Lecturer Ing. Marta Vohnoutová
# Homework No 12:
# Find and count the occurrence of all words in given text,
# sort them and print them to a file
#
# Author: Alexandre Lysov
# Date: April 21, 2017

import locale

allwords = list()
uniquewords = set()

try:
    
    nonalpha =  "!\"#$%&'()*+,-./0123456789:;<=>?@[\\]^_`{|}~„“–⊆×\ufeff\xa0" #remove these
    empty = " " * len(nonalpha)

    # 'with' block will automatically close files on exit from it
    with open("words_occurances.txt", "w") as wo:
        with open("/home/marta/IOS 655 Python a Bash/homework/Optimalizace-tvorby-rolí-pomocí-RBAC-modelu-v2.txt") as text:
            for line in text:
                line = line.strip()
                if (len(line) > 0):
                    line = line.translate(str.maketrans(nonalpha,empty)).strip()
                    # to include one letter words change condition to "> 0"
                    L = list( word for word in line.split(" ") if len(word.strip()) > 1 )
                    if (len(L) > 0):
                        for w in L:
                            allwords.append(w)
                            uniquewords.add(w)

        print("Output file will be sorted using locale: {}.".format(locale.getdefaultlocale()))
        uniquesort = sorted(list(uniquewords))

        for uw in uniquesort:
            wo.write( uw + " - " + str( allwords.count(uw) ) + "\r\n" )

except Exception as err:
    print(err)


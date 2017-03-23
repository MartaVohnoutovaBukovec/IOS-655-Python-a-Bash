#!/usr/bin/env python3

#Converts text files to the binary string files for usage by readbins.py

import os
import sys

def ascii2bins(text):
    """ This function converts text string to a binary string
    """

    s = text.strip()
    length = len(s)
    bins = ""
    
    if (length > 0):
        try:
            ba = s.encode("utf-8") #string to byte array
            for b in ba:
                bins += "{0:08b}".format(b) #each byte to a bynary string
            bins += "\r\n"
        except ValueError: 
            print("Conversion error to binary string: {0}".format(s), flush = True)
            return ""
                
    return bins


def readtext(filename):
    lines = []
    file = None
    try:
        file = open(filename, encoding="utf8")
        for line in file:
            s = ascii2bins(line)
            lines.append(s)
    except (IOError, OSError) as err:
        print(err)
        return []
    finally:
        if file is not None:
            file.close()
    return lines


def writebins(lines, filename):
    file = None
    try:
        file = open(filename, "w", encoding="utf8")
        for line in lines:
            file.write(line)
    except EnvironmentError as err:
        print(err)
    finally:
        if file is not None:
            file.close()

def main():
    
    if len(sys.argv) < 1:
        print("Usage: writebins.py in-file")
        sys.exit()

    for filename in sys.argv[1:]:
        lines = readtext(filename)
        if lines:
            writebins(lines, os.path.splitext(filename)[0] + ".bins")


main()

#!/usr/bin/env python3

# Subject: UAI / 655, Lecturer Ing. Marta Vohnoutová
# Homework No 1: read and translate binary strings to the original text
#
# Author: Alexandre Lysov
# Date: February 23, 2017
#
# This application reads text files, where each character of the text is represented 
# by a block of 8 binary characters (BYTE), e.i. '01001001...' with no separators.
#
# Parameter -i and file name are mandatory. 
# The decoded text from the file will be displayed to a standart output.
#
# If optional parameter -s is passed, the application will try to convert each line of the file
# to a '.wav' file and read it back in a loop. This feature requires working Internet connection.
# To conver text to speech the following libraries are needed 'pyaudio', 'wave', and 'requests'.
# However, these libraries are only being imported if the parameter -s is supplied.
#
# If speech is requested, but libraies are not istalled, the program will ignore -s.
#
# The application has been tested on Windows 10 with Python 3.5.3 with the speach option
# and on Ubuntu on Windows (so-called Bash on Windows 10) with Python 3.4.3 without speech.
# 

import argparse

def bins2ascii(bins):
    """ This function converts binary string to ASCII string
    """

    bs = bins.strip()
    length = len(bs)
    
    if (length % 8 != 0):
        print("Binary string doesn't have all 8 binary digits per charcter.", flush = True)
        print("Corrupted string: {0}".format(bs), flush = True)
        return ""
    else:       
        for b in bs:
            if (b not in ['0','1']):
                print("Wrong character '{0}' in binary string: {1}".format(b, bs), flush = True)
                return ""

        try:
            ba = int(bs, 2).to_bytes( length // 8, byteorder = 'big' )
            s = ba.decode("utf-8")

        except ValueError: 
            return ""
                
        return s
    

def readbins(filename):
    """ This function reads the file and returns list of strings from the file
    """
    
    lines = [] #create empty list
    infile = None
    try:
        infile = open(filename, encoding="utf8")
        for line in infile:
            s = bins2ascii(line) #decode the line
            if (len(s) > 0):
                lines.append(s)
    except (IOError, OSError) as err:
        print(err)
        return [] #return empty list if error
    finally:
        if infile is not None:
            infile.close()
    return lines #return all lines as a list


def main():
    """ Main function that processes arguments and calls other functions
    """

    parser = argparse.ArgumentParser(description='Decodes binary strings from the <in-file> to ASCII')
    parser.add_argument('-i', metavar='<in-file>', type=argparse.FileType('r'), required = True,
                        help = 'input file containing binary stings')
    parser.add_argument('-s', dest='boolean_speech', action='store_true',
                        default = False,
                        help = 'instructs the program to speak the decoded text back')

    # this statement will terminate the app
    # if file name was not supplied or file does not exist
    args = parser.parse_args()

    filename = args.i.name

    speech = args.boolean_speech

    decodedList = readbins(filename)

    if (speech):        
        # import classes for supporting speech only if we need them
        # '.py' modules are assumed to be in the same directory
        from playwave import playwave
        from apitts import apitts
        
        pw = playwave() # create playwave class object
        if (pw.canPlay): 
            tts = apitts() # create apitts class object
            speech = True
        else:
            speech = False
            
    # display or speak results
    i = 0
    for line in decodedList:
        print (line, flush = True)
        i += 1 #line counter
        if (speech):
            s = str(i)
            if (not tts.text2wave(line, s + ".wav")):
                # text2wave can fail for different reasons,
                # but most likely because of connectivity issues
                # On Linux there could be a long wait in case of timeout
                print("Cannot create '{0}.wav' file".format(s), flush = True)
            else:
                pw.play(s + ".wav")

    print("{0} lines were decoded.".format(i), flush = True)

main()




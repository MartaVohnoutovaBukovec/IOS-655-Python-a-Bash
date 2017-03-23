#!/usr/bin/env python3

# Subject: UAI / 655, Lecturer Ing. Marta Vohnoutová
# Homework No 3: display random number in big digits
#
# Author: Alexandre Lysov
# Date: March 3, 2017
#
# This application checks for input parameters:
# -n -min -max
# How to run: python3 ./randbign.py -n -5678 -min -7777 -max 77
# if a parameter '-n' is passed, then number is displayed (-min and -max are ignored)
# if -min, -max or both are passed and -n is not, then random number is displayed
# for n, maximum and minimum negative numbers are accepted
# -h or --help displays help
#
# The application has been tested on Windows 10 with Python 3.5.3 with the speach option
# and on Ubuntu on Windows (so-called Bash on Windows 10) with Python 3.4.3 without speech.
#

import argparse
import random

def loadBigDigits():
    
    zero = [" *** ","*   *","*  **","* * *","**  *","*   *"," *** "]
    one =  ["  *  "," **  ","* *  ","  *  ","  *  ","  *  ","*****"]
    two =  [" *** ","*   *","*  * ","  *  "," *   ","*    ","*****"]
    three =[" *** ","*   *","    *","  ** ","    *","*   *"," *** "]
    four = ["   * ","  ** "," * * ","*  * ","*****","   * ","   * "]
    five = ["*****","*    ","*    "," *** ","    *","*   *"," *** "]
    six =  [" *** ","*    ","*    ","**** ","*   *","*   *"," *** "]
    seven =["*****","    *","   * ","  *  "," *   ","*    ","*    "]
    eight =[" *** ","*   *","*   *"," *** ","*   *","*   *"," *** "]
    nine = [" ****","*   *","*   *"," ****","    *","    *"," *** "]

    lbd = [zero, one, two, three, four, five, six, seven, eight, nine]

    # replace stars with numbers
    for digit in range(0,10):
        for row in range(0,7):
            lbd[digit][row] = lbd[digit][row].replace("*",str(digit))
        
    return lbd

    
def main():
    """ Main function
    """

    parser = argparse.ArgumentParser(description='Displays big numbers')
    parser.add_argument('-n', dest='n_big', type=int, default = None,
                        help = 'number to be displayed')
    parser.add_argument('-min', dest='n_min', type=int, default = 0,
                        help = 'minimum random number ( + or -, default = 0)')
    parser.add_argument('-max', dest='n_max', type=int, default = 10000,
                        help = 'maximum random number, (+ or -, but >= N_MIN, default = 10000)')

    args = parser.parse_args() # parse arguments

    maximum = args.n_max
    minimum = args.n_min

    if (args.n_big is not None): # display passed number
        bignumber = args.n_big

    else: # display random number
        if (maximum < minimum): # fix data
            maximum = minimum

        bignumber = random.randint(minimum, maximum) # get random number

    listOfBigDigits = loadBigDigits()

    if (bignumber < 0): # define minus as big number
        minus =["     ","     ","     "," --- ","     ","     ","     "]

    try:

        strnumber = str(abs(bignumber)) # removing minus from the string of numbers
        strlength = len(strnumber)

        for row in range(0,7): # for each row to print

            if (bignumber < 0):
                newline = minus[row] # add minus if needed
            else:
                newline = "  " # or get empty line
                
            for digit in range(0,strlength): # for each digit in string

                n = int(strnumber[digit]) # convert it to integer
                newnumber = listOfBigDigits[n] # obtain bignumber for n
                newline += newnumber[row] + "  " # add corresponding row to newline

            print(newline) # when all substrings are added to newline we can print it

    except ValueError as error:
        print(error)

main()


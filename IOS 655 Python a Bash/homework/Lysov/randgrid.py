#!/usr/bin/env python3

# Subject: UAI / 655, Lecturer Ing. Marta Vohnoutová
# Homework No 2: generate grid of random numbers
#
# Author: Alexandre Lysov
# Date: March 3, 2017
#
# This application checks for input parameters:
# -row, -col, -max, -min
# How to run: python3 ./randgrid.py -min -77 -max -7 -row 10 -col 8
# if a parameter is not passed, the default value is used
# for maximum and minimum negative numbers are accepted
# -h or --help displays help
#
# The application has been tested on Windows 10 with Python 3.5.3 with the speach option
# and on Ubuntu on Windows (so-called Bash on Windows 10) with Python 3.4.3 without speech.
#

import argparse
import random

def main():
    """ Main function
    """

    parser = argparse.ArgumentParser(description='Generates grid of random numbers')
    parser.add_argument('-row', dest='n_rows', type=int, default = 5,
                        help = 'number of rows in the grid: 1 - N (default = 5)')
    parser.add_argument('-col', dest='n_cols', type=int, default = 5,
                        help = 'number of columns in the grid: 1 - 10 (default = 5)')
    parser.add_argument('-min', dest='n_min', type=int, default = 0,
                        help = 'minimum random number ( + or -, default = 0)')
    parser.add_argument('-max', dest='n_max', type=int, default = 10000,
                        help = 'maximum random number, (+ or -, but >= N_MIN, default = 10000)')

    args = parser.parse_args() # parse arguments

    # test arguments
    rows = args.n_rows
    if (rows < 1):
        rows = 1
    cols = args.n_cols
    if (cols < 1):
        cols = 1
    if (cols > 10):
        cols = 10

    maximum = args.n_max
    minimum = args.n_min
    if (maximum < minimum):
        maximum = minimum

    cell_size = len(str(maximum)) + 1 # +1 is for sign
    sep_size = (cell_size + 2) * cols # horizontal separator size

    # create array of random numbers
    arrOfRandNumbers = [ random.randint(minimum, maximum)
                         for n in range(0, rows * cols) ]
    
    # print formatted grid
    for n in range(0, rows * cols):
        if ( n % cols == 0 ): 
            if ( n > 0 ):
                print ("|") #vertical separator
            # horizontal separator
            print("+{0:->{size}}".format("+",size = sep_size))
        # value
        print("|{0: >{size}}".format(arrOfRandNumbers[n], size = cell_size), end = " " )
    #last verical and horizontal separators
    print("|\n+{0:->{size}}".format("+", size = sep_size))


main()


"""
Author: Kareem Jeiroudi
Date: 19.03.2017
Title: Gride Generation with Random Numbers
"""
# for generating random integers
import random

def make_grid():
    # variables to input user's choice of the grid details.
    # have anyways default values, in case the user didn't input anything at all.
    rows, columns = 1, 1
    mini, maxi = 0, 100

    # reading values from keyboard using the input function.
    rows = input ("How many rows do you want your grid to have? ")
    columns = input ("How many rows do you want your grid to have? ")
    mini = input ("What is the smallest number that can appear in your grid? ")
    maxi = input ("What is the biggest number that can appear in your grid? ")

    try:
        # genrate one row, consisting of as many items as the columns
        ar = [
            [[random.randint(int(mini), int(maxi))] for t in range(int(columns))]
            for i in range(int(rows))
            ]
        
        # print out the row and make a line break
        for row in ar:
            print(row)
    except ErrorValue:
        print("One or some of the values you inserted are not valid as integers")

# calling the function
make_grid()

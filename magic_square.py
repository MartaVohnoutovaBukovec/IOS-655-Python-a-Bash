
"""
Magic square

"""

__author__ = 'Marta Vohnoutova'
__version__ = '0.1'

#===============================================================================
# IMPORTS
#===============================================================================
import numpy as np


#===============================================================================
# METHODS
#===============================================================================

def new_matrix(n):
    matrix = np.random.permutation(np.arange(1,(n*n)+1)).reshape(n,n)
    return matrix

def checking(matrix,n):
    check = True
    number = (n*(n*n+1))/2

    rows = np.sum(matrix, axis=1)       
    columns = np.sum(matrix, axis=0)
    for i in range(n):                  #rows
        if rows[i] != number:
            check = False   
            break
       
    if check:                           #columns
        for i in range(n):
            if columns[i] != number:
                check = False
                break
    if check:                       # diagonals
        suma = 0
        for i in range(n):
            suma += matrix[i][i]
        if suma != number:
            check = False
            
    if check:                       # diagonals
        suma = 0
        for i in range(n):
            suma += matrix[i][n-i-1]
        if suma != number:
            check = False
            
    return check

def fill_square(n):
    while True:
        matrix = new_matrix(n)
        if checking(matrix,n):
            break
        
    return matrix
    

#===============================================================================
# MAIN PROGRAM
#===============================================================================

n = int(input("N :"))
                                            
square_matrix = fill_square(n) # fill square matrix and check if it is magic
print(square_matrix)




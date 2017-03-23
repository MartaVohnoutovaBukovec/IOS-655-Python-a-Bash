#!/usr/bin/env python3

# Subject: UAI / 655, Lecturer Ing. Marta Vohnoutová
# Homework No 3: display random number in big digits
#
# Author: Marta Vohnoutova
# Date: March 4, 2017

import random

dig = {"0": [" *** ","*   *","*  **","* * *","**  *","*   *"," *** "],
    "1": ["  *  "," **  ","* *  ","  *  ","  *  ","  *  ","*****"],
    "2": [" *** ","*   *","*  * ","  *  "," *   ","*    ","*****"],
    "3": [" *** ","*   *","    *","  ** ","    *","*   *"," *** "],
    "4": ["   * ","  ** "," * * ","*  * ","*****","   * ","   * "],
    "5": ["*****","*    ","*    "," *** ","    *","*   *"," *** "],
    "6": [" *** ","*    ","*    ","**** ","*   *","*   *"," *** "],
    "7": ["*****","    *","   * ","  *  "," *   ","*    ","*    "],
    "8": [" *** ","*   *","*   *"," *** ","*   *","*   *"," *** "],
    "9": [" ****","*   *","*   *"," ****","    *","    *"," *** "]}


d=str(random.randrange(0, 999999))
print(d, "was generated \n")

for row in range(0,7):
    for i in d:
        print(dig.get(i)[row].replace("*",i),end=" ")
    print()
    
        

    




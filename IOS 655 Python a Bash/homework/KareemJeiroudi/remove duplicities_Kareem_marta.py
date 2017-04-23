"""
# Author: Kareem Jeiroudi
# Data: 05.04.2017
# Version: 0.1
# Marta revised
#
"""
d3= [("x",3, "y",3),("x",2, "y",-1),("x",2, "y",3),("x",-1, "y",0),("x",2, "y",2),("x",3, "y",-1),("x",1, "y",2),("x",0, "y",2),("x",1, "y",0),("x",0, "y",-1),("x",0, "y",1),("x",-1, "y",0),("x",1, "y",-1),("x",-1, "y",1),("x",2, "y",0),("x",1, "y",2),("x",-1, "y",0),("x",1, "y",2),("x",-1, "y",3),("x",-1, "y",2),("x",0, "y",0),("x",1, "y",3),("x",2, "y",0),("x",0, "y",2),("x",-1, "y",-1),("x",0, "y",2),("x",2, "y",3),("x",2, "y",-1),("x",2, "y",0),("x",3, "y",3),("x",-1, "y",0),("x",2, "y",-1),("x",0, "y",-1),("x",2, "y",2),("x",-1, "y",0),("x",2, "y",-1),("x",0, "y",1),("x",0, "y",3),("x",3, "y",1),("x",0, "y",2),("x",2, "y",0),("x",0, "y",2),("x",1, "y",2),("x",0, "y",3),("x",1, "y",0),("x",-1, "y",0),("x",-1, "y",3),("x",1, "y",-1),("x",0, "y",2),("x",2, "y",3),("x",-1, "y",1),("x",1, "y",0),("x",2, "y",3),("x",2, "y",2),("x",1, "y",2),("x",0, "y",-1),("x",-1, "y",1),("x",1, "y",0),("x",0, "y",2),("x",3, "y",3),("x",2, "y",-1),("x",1, "y",3),("x",2, "y",3),("x",1, "y",2),("x",3, "y",0),("x",0, "y",2),("x",3, "y",0),("x",0, "y",-1),("x",3, "y",3),("x",1, "y",3),("x",-1, "y",-1),("x",1, "y",1),("x",0, "y",3),("x",3, "y",-1),("x",1, "y",2),("x",1, "y",0),("x",-1, "y",0),("x",2, "y",3),("x",1, "y",-1),("x",0, "y",0),("x",0, "y",1),("x",1, "y",1),("x",-1, "y",1),("x",-1, "y",0),("x",2, "y",-1),("x",1, "y",-1),("x",3, "y",-1),("x",2, "y",1),("x",0, "y",1),("x",1, "y",1),("x",3, "y",1),("x",2, "y",3),("x",1, "y",3),("x",1, "y",3),("x",1, "y",-1),("x",2, "y",1),("x",0, "y",1),("x",3, "y",0),("x",1, "y",-1),("x",3, "y",-1)]

# the first function will remove all duplicities that are
# inside the tuples, however, won't affect the tuples.
# leading to the same amount of tuples but sometimes with less items.

def removeDuplicities(para):
    try:
        curList = []
        for tup in para:
            try:
                curList.index(tup)
            except ValueError:
                curList.append(tup)
        return curList
    # return an error if no value is given to the parameter.
    except ValueError:
        print("No parameter is inserted to the function!")

print(removeDuplicities(d3))

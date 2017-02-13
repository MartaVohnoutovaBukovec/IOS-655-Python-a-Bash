# ch08_02.py
# reading file

import sys

#####################################
print('opening files...')

f1 = open('mydoc1', 'r')
f2 = open('mydoc2', 'r')
bf1 = open('mydoc3', 'rb')
bf2 = open('mydoc4', 'rb')


#####################################
# reading data

def reading_data(f):
    while True:
        data = f.readline()
        if (data == '') or (data == None):
            break

        sys.stdout.write(data)


print('for mydoc1>>>>>')
reading_data(f1)
print('>>>>>>>>>>>>>>>')

print('for mydoc2>>>>>')
reading_data(f2)
print('>>>>>>>>>>>>>>>')

print('for mydoc3>>>>>')
reading_data(bf1)
print('>>>>>>>>>>>>>>>')

print('for mydoc4>>>>>')
reading_data(bf1)
print('>>>>>>>>>>>>>>>')

#####################################
# close all

print('close files...')
f1.close()
f2.close()
bf1.close()
bf2.close()

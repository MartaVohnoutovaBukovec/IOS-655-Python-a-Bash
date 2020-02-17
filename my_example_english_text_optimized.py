#marta vohnoutova 
'''
english text

'''
# import libraries
import re
import string as st
import random as rd
import secrets as sc
import math
from collections import OrderedDict as od  # to keep the order in dictionary
from collections import deque

# constants
letters=st.ascii_lowercase + ' '+'\n'
how_many_letters = 15
#up_to=6115909
up_to=1000000

# files

source_file_in = 'big_english.txt'
source_adjusted_file_in = '1000000_english_adjusted.txt'
random_file_in = 'random_ab_english.txt'

# data input preparing
# adjust the text file for processing and pick up all letters

'''
f_out=open(source_adjusted_file_in,'w')

with open(source_file_in,'r') as f_in:
   line = f_in.readline()
   cnt=0
   while line:
       for i in line:
           if i in letters:
               f_out.write(i.lower())
               cnt += 1
       line = f_in.readline()
       
       if cnt >= up_to:
           break
   
       
f_out.close()
f_in.close()
'''

# create the real random file for comparison, same length
cnt=up_to

f_out=open(random_file_in,'w')
for i in range(cnt):
    # f_out.write(sc.choice(letters))
    if i%2:
        f_out.write('A')
    else:
        f_out.write('B')
f_out.close()


# methods

def count_mod_and_stat(adjusted_file_in, part_of_letters):         #Markov
    d_stat=od()
    d_mod=od()
    
    f_in=open(adjusted_file_in,'r')
    rows_in = f_in.read()
          
    moving_window = deque(maxlen = part_of_letters)
    
    for j in rows_in:
            
        key=''.join(moving_window)
        moving_window.append(j)
##      print(part_of_letters,key)
        if len(key) == part_of_letters:
            if key not in d_mod:
                d_mod[key] = od()
                                  
            if j in d_mod[key]:
                d_mod[key][j] += 1                   
            else:
                d_mod[key][j] = 1                   
                
            if key in d_stat:
                d_stat[key] += 1
            else:                    
                d_stat[key] = 1
 
    f_in.close()
    return d_mod,d_stat

# count entropy and entropy rate for each number of letters 

def entropy_for_key(d_mod_part, d_stat_part):
	return -sum(v / d_stat_part * math.log2(v / d_stat_part) for v in d_mod_part.values())

def entropy_rate(model, stats):
	return sum(stats[stat] * entropy_for_key(model[stat], stats[stat]) for stat in stats) / sum(stats.values())

   
# program body
'''
print('Big English 6.140.000 letters - entropy rates')

for i in range(1,how_many_letters+1):
    d1_mod,d1_stat = count_mod_and_stat(source_adjusted_file_in,i)   # mod and stat big english
    print('Entropy rate for {0} is {1:.15f}'.format(i,entropy_rate(d1_mod, d1_stat)))
'''

print('Random regular ASCII AB letters - entropy rates')
for i in range(1,how_many_letters+1):
    d2_mod,d2_stat = count_mod_and_stat(random_file_in,i)   # random ascii letters
    print('Entropy rate for {0} is {1:.15f}'.format(i,entropy_rate(d2_mod, d2_stat)))


# input information
# input note = only numbers and capital letters are used in lists 
number_input = input("Please enter a number: ")
from_base = int(input("Enter the base FROM which you would like to convert the number:  "))
to_base = int(input("Please enter the base TO which you would like to convert your number:  "))

# list_of_elements = list with digits and letters and their assigned values

list_of_elements ={'0': 0, '1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18,'J': 19,   'K': 20,'L': 21,'M': 22,'N': 23,'O': 24,'P': 25,'Q': 26,'R': 27,'S': 28,'T': 29,'U': 30,'V': 31,'W': 32,'X': 33,'Y': 34,'Z': 35}

digit = 0
for element in number_input:
    value = list_of_elements[element]             
    digit = digit * from_base
    digit = digit + value

# values_for_list =  list of values and digits/letters assigned to them    

values_for_list = dict(map(reversed, list_of_elements.items()))

final_list = []
while digit:
    digit, value = divmod(digit, to_base)       #using of buildin function = divmod(quotient,remainer)
    final_list.append(values_for_list[value])
result = ''.join(reversed(final_list))
print (result)

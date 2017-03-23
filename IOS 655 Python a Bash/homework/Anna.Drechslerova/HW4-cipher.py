i = input("Please give me input : ").upper()
k = input("Please give me keyword:").upper()
e_d = str(input("Would you like to encrypt or decrypt the input ? (write 'e' for encrypt or 'd' for decrypt): "))

#part of program valid for encryption and decryption
m=i.replace(" ", "")            #deletes spaces
print(m)                        #prints out the string without spaces
l= len(m)
repeat_k=(k * l)[0:l]
print(repeat_k)        #prints out the keyword modified for input lenght = just to make sure its working correctly
alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"  #variable which contains string with alphabet

  #if the user wants to encrypt input
 
if e_d == "e":
 print("New encrypted string:")
 for n in range(0,l):
   loc_e = m[n]                       # variable "loc_e" gives us the character in "m" string for "n" index 
   pos_e = repeat_k[n]
   if alph.find(loc_e):
     index_m=alph.index(loc_e)
   if alph.find(pos_e):
     index_k=alph.index(pos_e)
   eq = (index_m + index_k)%26      #eq = equation for adding indexes and % of letters in the alphabet (26)
   new_letter=alph[eq]                #new_letter = index for new coded letter
   encrypted=[new_letter]
   encrypted_string=''.join(encrypted) 
   print(encrypted_string,end="")

 #if the user wants to decrypt input
   
if e_d == "d":                     
 print("New decrypted string:")
 for n in range(0,l):
   loc_d = m[n]                       # variable "loc_d" gives us the character in "m" string for "n" index 
   pos_d = repeat_k[n]
   if alph.find(loc_d):
     index_m=alph.index(loc_d)
   if alph.find(pos_d):
     index_k=alph.index(pos_d)
   eq = (index_m - index_k)%26      #eq = equation for substracting indexes and % of letters in the alphabet (26)
   new_letter=alph[eq]                #new_letter = index for new coded letter
   encrypted=[new_letter]
   encrypted_string=''.join(encrypted) 
   print(encrypted_string,end="")

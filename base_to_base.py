# any base to any base function example
# Function definition is here
def base_to_base(s_in,b_in,b_out):
   return str_base(int(str(s_in),b_in),"0123456789abcdefghijklmnopqrstuvwxyz"[:b_out])
   

def str_base(number, base):
   (d,m) = divmod(number, len(base))
   if d > 0:
      return str_base(d,base)+base[m] 
   
   return base[m]



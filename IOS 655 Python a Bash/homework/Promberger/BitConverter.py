BitInput=input("Please enter the Bit code:")
for bit in range(0,len(BitInput),8):
    byte=""
    for i in range(0,8):
        byte+=BitInput[bit+i]
    print(chr(int(byte,2)), end="")
    

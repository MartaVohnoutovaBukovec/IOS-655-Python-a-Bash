# example7 modulo11 verifying text file Marta
# w=[6,3,7,9,10,5,8,4,2,1]


def modulo11_check(account):
    r_account=list(reversed(account))
    s=0
    for i in (range(len(r_account))):
        s += int(r_account[i])*((2**(i+1))%11)
    if s % 11 == 0:
        return True
    else:
        return False

f = open("accounts.txt","r")
f_out = open("accounts_verified.txt","w")
i=0

for line in f:
    l=line.split("/")
    if not modulo11_check(l[0]):
        print("Not compatible account: ",line)
    else:
        f_out.write(line)
        
        
f.close()
f_out.close()    

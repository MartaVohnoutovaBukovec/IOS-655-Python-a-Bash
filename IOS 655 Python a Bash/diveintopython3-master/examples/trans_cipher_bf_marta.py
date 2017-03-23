# Trans cipher with key brute force
# Marta Vohnoutova


def trans_cipher_bf(string,keyword):

    keys = keyword
    string_en=""
      
    for i in range(0,len(string),len(keys)):
        for j in keys:
            try:
                string_en += string[i+ int(j)]
            except IndexError:
                pass       
    
    return string_en                               

import random
import itertools
from operator import itemgetter, attrgetter

s="ne Ocpn uo idamihtngdea ry wr,ie hl onIpeeddr ea,w ndkawar e,veyO anrm  \
qyaantuiad  nuiocrsvou ue lmffoo gttronloe e Wr—ie hl odIne, dderlna \
apynig,pnsdd uny elhretecme aata  pngpi s ,Afsoo eonm  enegl rtypinap,\
rag pngpia m t haycbr meor.doTs  ioe smiitvsr Io,mtt urd,eetpp an aig y \
tmhmbcardoe r Oo—l tnyi ahsdnon hngtimre o   . "

f=open('transcipher_bf_marta.txt', 'w')

for x in [''.join(p) for p in itertools.permutations('01234')]:
    f.writelines(trans_cipher_bf(s,x))
    f.write("\n {} \n".format(x))

f.close()

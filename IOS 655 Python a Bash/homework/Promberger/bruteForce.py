import TranspositionCipher
def getPermutations(array,i,n):
    if(i==n):
        return array
    else:
        try:
            for j in range(i,n,1):      #still prduces some duplicates, but im not sure why
                array[j],array[i]=array[i],array[j]
                getPermutations(array,i+1,n)
                array[j],array[i]=array[i],array[j]
        except IndexError:
            pass
    #print(array)
    outputStr="".join(array)
    TranspositionCipher.transpositionCipher("ne Ocpn uo idamihtngdea ry wr,ie hl onIpeeddr ea,w ndkawar e,veyO anrm  qyaantuiad  nuiocrsvou ue lmffoo gttronloe e Wr—ie hl odIne, dderlna apynig,pnsdd uny elhretecme aata  pngpi s ,Afsoo eonm  enegl rtypinap,rag pngpia m t haycbr meor.doTs  ioe smiitvsr Io,mtt urd,eetpp an aig y tmhmbcardoe r Oo—l tnyi ahsdnon hngtimre o   . ",outputStr,0)
    return outputStr
a=["A","B","C","D","E"]
key=getPermutations(a,0,5)
#Key: DAEBC
#Once upon a midnight dreary, while I pondered, weak and weary,Over many a quaint and curious volume of forgotten lore—
#While I nodded, nearly napping, suddenly there came a tapping, As of some one gently rapping, rapping at my chamber door.
#Tis some visitor, I muttered, tapping at my chamber door— Only this and nothing more.    

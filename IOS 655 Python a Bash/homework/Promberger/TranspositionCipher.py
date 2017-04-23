def transpositionCipher(inStr, key, en):
    output=""
    if en:
        key=key.upper()
        array=[""]*len(key)
        try:
            for i in range(len(inStr)): #dividing the input String into "columns"
                index=i%len(key)    #returns values from 0 to key-1
                array[index]+=inStr[i]
        except IndexError:
            pass
        dic={key[i]:array[i] for i in range(len(key))}  #creates a dictionary which contains the array to each key letter
        #print(dic)
        try:
            for j in range(0,len(inStr),len(key)): #iterates threw the dictionary with steps of key lenght
                for i in sorted(dic): #sorts the dictionary and therfore encrypts it
                    output+=dic[i][j//len(key)] #adds the letter to the output String
            print(output)
        except IndexError:
            pass
    else:
        array=[""]*len(key)
        keynew="".join(sorted(key.upper()))
        key=key.upper()
        try:
            for i in range(len(inStr)):
                index=i%len(key)
                array[index]+=inStr[i]
        except IndexError:
            pass
        dic={keynew[i]:array[i] for i in range(len(key))}
        for i in range(0,len(inStr),len(key)):
            try:
                for k in key:
                    for d in dic:
                        if(ord(k)==ord(d)):
                            output+=dic[d][i//len(key)]
            except IndexError:
                pass
        print(key)
        print(output)


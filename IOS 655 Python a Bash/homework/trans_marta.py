def getKey(item):
	return item[1]

def trans_cipher(string,keyword,en):

    from operator import itemgetter, attrgetter

    k = list(enumerate(keyword.upper()))    
    k = sorted(k, key=itemgetter(1))
    keys = [(i,k[i][0]) for i in range(len(k))]
    string_en=""

    if en:           
        for i in range(0,len(string),len(keys)):
            for j in keys:
                try:
                    string_en += string[i+j[1]]
                except IndexError:
                    pass
    else:
      
        keys = sorted(keys,key=getKey)        
        for i in range(0,len(string),len(keys)):
            for j in keys:
                try:
                    string_en += string[i+j[0]]
                except IndexError:
                    pass       
    
    return string_en               

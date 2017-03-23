def basetobase(number, basein, baseout):
    numberDec=int(number,basein)
    numberStr = "0123456789abcdefghijklmnopqrstuvwxyz"
    numberOut=""
    while (numberDec > 0):
        numberOut+=numberStr[int(numberDec%baseout)]
        numberDec = numberDec//baseout      
    print(numberOut[::-1])


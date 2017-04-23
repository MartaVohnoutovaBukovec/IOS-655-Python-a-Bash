# substitution cipher brure force
# stephan moser

def getEncryptedMessage():
    # return input("Enter encrypted message:")
    return "ECPUA WHMPQE ANXAE AP UNHF OV NVBZOEC WUPM LZHEEOL EPQULNE ZOKN ACN TOTZN PU ECHKNEDNHUN ROAC RPUF FNWOVOAOPVE HVF NXDZHVHAOPVE AP CNZD GPQ CNUN HUN EPMN AUHFOAOPVHZ EHGOVBE ACHA HUN RNZZ KVPRV AP NVBZOEC EDNHKNUE EPMN PW ACNM LPMN WUPM PACNU ZHVBQHBNE TQA ACNG HUN WUNYQNVAZG QENF OV NVBZOEC"

def getIndexForWord(word):
    index = dict()
    count = 0
    for char in word:
        if not char in index:
            index[char] = count
            count += 1
    
    return "".join(str(index[c]) for c in word)

def getLangDict(path):
    indexDict = dict()
    for line in open(path, "r"):
        withOutNewLine = line.replace("\n", "")
        index = getIndexForWord(withOutNewLine)
        if index in indexDict:
            indexDict[index].append(withOutNewLine)
        else:
            indexDict[index] = [withOutNewLine]
           
    return indexDict

def translationCollidsWithDict(encryptedWord, translation, transDict):
    for i in range(0,len(translation)):
        if encryptedWord[i] in transDict and transDict[encryptedWord[i]] is not translation[i]:
            return True
        if encryptedWord[i] not in transDict and translation[i] in transDict.values():
            return True
    return False

def removeImpossibleIndex(untranslatedWords, langDict):
    wordsToRemove = []
    for word in untranslatedWords:
        if getIndexForWord(word) not in langDict:
            
            wordsToRemove.append(word)
    for word in wordsToRemove:
        untranslatedWords.remove(word)

def writeIntoTransDict(encryptedWord, decryptedWord, transDict):
    for i in range(0,len(encryptedWord)):
        if not encryptedWord[i] in transDict:
            transDict[encryptedWord[i]] = decryptedWord[i]
    return transDict

def getUniqueTranslation(word, langDict, transDict):
    validTranslations = list()
    for translation in langDict[getIndexForWord(word)]:
        if not translationCollidsWithDict(word, translation, transDict):
            validTranslations.append(translation)
    if len(validTranslations) == 1:
        return validTranslations[0]
    return ""

def translateWords(words,langDict, transDict):
    wordsToRemove = []
    for word in words:
        uniqueTranslation = getUniqueTranslation(word, langDict,transDict)
        if uniqueTranslation is not "":
            print(word, uniqueTranslation)
            writeIntoTransDict(word, uniqueTranslation, transDict)
            wordsToRemove.append(word)
            
    if len(wordsToRemove) == 0:
        return
            
    for word in wordsToRemove:
        words.remove(word)
    
    if len(words) > 0:
        translateWords(words,langDict,transDict)
    
def main():
    transDict = {" ": " "}
    langDict = getLangDict("/home/marta/IOS 655 Python a Bash/homework/Moser/dict.txt")
    message = getEncryptedMessage()
    
    untranslatedWords = sorted(message.split(" "),key=len,reverse=True)    
    removeImpossibleIndex(untranslatedWords, langDict)
    translateWords(untranslatedWords, langDict, transDict)
    
    print("".join(transDict.get(c,"?") for c in message))
    

    print(transDict)
    
main()

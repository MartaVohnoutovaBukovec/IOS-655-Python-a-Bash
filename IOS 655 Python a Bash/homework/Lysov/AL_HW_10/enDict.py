#!/usr/bin/env python3
#
# Subject: UAI / 655, Lecturer Ing. Marta Vohnoutová
# Homework No 10: create a program that breaks the substitution cipher
# using 'brute force' approach by seeking patterns in the English dictionary
#
# Author: Alexandre Lysov
# Date: April 2017
#

import sqlite3

class enDict:
    """ This class operates dictDb
    """
    pass

    def __init__(self):

        self.__dbPath = ""
        self.__conn = None
        self.__cursor = None
        self.__count = 0


    def __del__(self):

        if (self.__conn is not None):
            self.__conn.commit()
            self.__conn.close()

    @property
    def count(self):
        """ returns number of records in the dictionary.
        """
        return self.__count

    def findAll(self, s, ch):
        """ returns list of positions of a character in a message
        """    
        return [i for i, c in enumerate(s) if c == ch]

    def topLetter(self, msg):
        """ Calculates letter of highest frequency in a message
        """
        
        MF = list()
        mlen = len(msg) - msg.count(" ")
        for c in "QWERTYUIOPASDFGHJKLZXCVBNM":
            MF.append((c,round(msg.count(c)/mlen*100,2)))
        # sort by percentage in descending order
        MF = sorted(MF, key = lambda item: item[1], reverse = True)

        return MF[0][0] 

    def access(self, path):
        """ This function opens connection to the dictionary database.
            It creates table and indeces if they do not exist.
        """

        self.__dbPath = path.strip()
        
        try:
            self.__conn = sqlite3.connect(self.__dbPath)
            self.__conn.execute("CREATE TABLE IF NOT EXISTS en_dict ("
                                "word TEXT PRIMARY KEY,"
                                "pattern TEXT NOT NULL);")
            self.__conn.commit()

            self.__conn.execute("CREATE INDEX IF NOT EXISTS idx_pattern "
                                "on en_dict (pattern);")
            self.__conn.commit()

            #self.__conn.execute("VACUUM;")

        except sqlite3.Error as err:
            print(err)
            return 1

        self.__recordcount()

        if (self.__count == 0):
            self.load("en_words.txt")
            self.__recordcount()
            print("{} records loaded.".format(self.__count))
           
        return 0


    def get_pattern(self, word):
        """ This function calculates letter pattern in a word.
            It returns a tuple of original word and its pattern.
        """

        temp = ""
        pattern = ""

        for c in word:
            if (c not in temp):
                temp += c
            pattern += str(temp.find(c))
                
        return (word,pattern)


    def load(self, filename):
        """ This function loads the dictioanry of words and their patterns
            !!! Loading file must contain only one word per line and only letters !!!
        """
        print("Loading dictionary. Please wait ...")
        infile = None 
        if (self.__conn is not None):
            try:
                infile = open(filename, encoding="utf8")
                for line in infile:
                    word = line.replace("\n","").upper()
                    if ("'" not in word):
                        self.__cursor = self.__conn.cursor()
                        self.__cursor.execute("SELECT word FROM en_dict " 
                                              "WHERE word = '%s';" % word)
                        if (self.__cursor.fetchone() is None):
                            self.__conn.execute("INSERT INTO en_dict VALUES (?,?);",
                                                  self.get_pattern(word))
                self.__conn.commit()
                self.__conn.execute("VACUUM;")

            except (IOError, OSError, sqlite3.Error) as err:
                print(err)
            finally:
                if infile is not None:
                    infile.close()

        self.__recordcount()

    def __recordcount(self):

        if (self.__conn is not None):
            try:
                self.__cursor = self.__conn.cursor()
                self.__cursor.execute("SELECT COUNT(*) FROM en_dict;")
                self.__count = self.__cursor.fetchone()[0]
            except sqlite3.Error as err:
                print(err)

    def get_matches(self, pattern, positions, s):
        
        __strSql = "SELECT word FROM en_dict where pattern = '{}'".format(pattern[1])
        for p in positions:
            __strSql += " AND substr(word, {} ,1) = 'E'".format(p+1)
        __strSql += ";"

        if (self.__conn is not None):
            try:
                self.__cursor = self.__conn.cursor()
                recordset = self.__cursor.execute(__strSql).fetchall()
            except sqlite3.Error as err:
                print(err)

            rc = len(recordset)
            if (rc != 0):
                
                eLetter = ""
                
                for i in range(len(pattern[0])): # for current encrypted word
                    eLetter = pattern[0][i] # take each letter
                    counts = [ [c,0] for c in "QWERTYUIOPASDFGHJKLZXCVBNM" ]
                    
                    # for each word in dictionary that matches the pattern
                    for j in range(0, rc):
                        word = "".join(recordset[j]) 
                        for k in range(len(counts)): #calculate occurences of letters
                            if (counts[k][0] == word[i]):
                                counts[k][1] += 1
                                break

                    # convert occurences to frequences
                    for l in range(len(counts)):
                        if (counts[l][1] != 0):
                            dLetter = counts[l][0]
                            frequency = round(counts[l][1]/rc*100,2)
                            if (frequency == 100.0): # only direct hits
                                # this set was passed as a parameter
                                s.add((eLetter,dLetter,frequency)) 
            

    def use_z_force(self, words, str1, str2, msg):
                
        loop = 12 # we need some limit of tries
        multirecord = False
        reminder = str2.count("_")
        unresolved = set()
        last_count = 0
        
        while True: # maximum of <loop> times
            
            for item in words: # for each word starting

                positions = self.findAll(item[1], "_")
                if (len(positions) == 0): # fully translated word
                    continue

                # underscore "_" replaces eny single letter for LIKE clause
                __strSql = "SELECT word FROM en_dict where word LIKE '{}'".format(item[1])

                if (self.__conn is not None):
                    try:
                        self.__cursor = self.__conn.cursor()
                        recordset = self.__cursor.execute(__strSql).fetchall()
                    except sqlite3.Error as err:
                        print(err)

                    rc = len(recordset)
                    if (rc != 0):
                        # print(item, recordset)
                        if (rc == 1): # direct hit !!! Substitute missing letters
                            w = "".join(recordset[0])

                            for p in positions: # update key
                                j = str1.find(item[0][p])
                                str2 = str2[:j] + w[p] + str2[j+1:]

                                l = len(str1)+5
                                print("DEC: {}".format(str1))
                                print("ENC: {}".format(str2))
                                print("-" * l)
                                
                            # re-translate all words with updated key
                            for word in words:
                                word[1] = word[0].translate(str.maketrans(str1,str2))
                            
                        else: # multiple records for pattern
                            if (multirecord): # only if direct hits no longer work
                                rs = []
                                for record in recordset:
                                    for p in positions: # remove all records with used letters
                                        if (record[0][p] not in str2):
                                            rs.append(record)
                                            
                                if (len(rs) == 1): # if removal leaves one record
                                    w = "".join(rs[0])
                                    for p in positions: # update key
                                        j = str1.find(item[0][p])
                                        str2 = str2[:j] + w[p] + str2[j+1:]
                                        
                                    l = len(str1)+5
                                    print("DEC: {}".format(str1))
                                    print("ENC: {}".format(str2))
                                    print("-" * l)
                                    
                                    # re-translate all words with updated key
                                    for word in words:
                                        word[1] = word[0].translate(str.maketrans(str1,str2))
                                        
                                else: # otherwise give up
                                    unresolved.add((item[1],str(rs)))


            loop = loop - 1
            newreminder = str2.count("_")
            new_count = len(unresolved)
            
            if (newreminder == 0 or loop == 0):
                break
                
            if (newreminder == reminder): # no more improvement in single records analisys
                if ( not multirecord ):
                    multirecord = True # switch to multi record analysis
                else:
                    if (new_count == last_count): # no more improvement in multiple records analisys
                        break

            last_count = new_count                
            reminder = newreminder
                   
        if (newreminder == 0):
            print("Fully decrypted message:")
        else:
            new_count = len(unresolved)
            if (new_count > 0):
                print("\nThe following {} word(s) cannot be resolved by brute force:".format(new_count))
                for u in unresolved:
                    print(u)
                print("\nSemantic level of analysis is required.\n")
                print("Partially decrypted message:")

        return msg.translate(str.maketrans(str1,str2))

    def decipher(self, msg):
            
        print("***************************")
        print("Finding direct 100% hits...")
        print("***************************")
        
        # create unique list of words and patterns sorted by length in descending order
        # the longer the word, the less hits we are going to get for each pattern
        eList = sorted(list(set( self.get_pattern(word) for word in msg.split(" "))),
                      key = lambda item: len(item[0]), reverse = True)                 

        topL = self.topLetter(msg)
        # loop through all words starting from the longest one
        S100 = set() # matches with 100% hits
        # S100 is being updated by get_matches
        for item in eList:
            pos = self.findAll(item[0], topL)
            self.get_matches(item, pos, S100)

        # find matches of 100% hits
        str101 = "".join([ item[0] for item in S100 ])
        str102 = "".join([ item[1] for item in S100 ])
        assert len(str101) == len(str102), "Wrong key length. Cannot continue."

        # find unique letters from the message
        letters = "".join(list(set ( c for c in msg if c != " ")))
        
        # build our first key (str102)
        for letter in letters:
            if (letter not in str101):
                str101 += letter
                str102 += "_"
                
        eL = msg.split(" ") # split encrypted message
        # make first translation based on 100% hits
        dL = msg.translate(str.maketrans(str101,str102)).split(" ")
        assert len(eL) == len(dL), "Wrong msg length. Cannot continue."
        # make it unique as a set
        s = set()
        for i in range(len(eL)):
            s.add((eL[i],dL[i]))

        # make it updatable as a list of words and translations with 100% hits
        L = [ [item[0], item[1]] for item in s ]

        # this is our initial sorted list from logest word to shortest
        # sorting allows to strat with longer words, which speeds up the process
        L100 = sorted(L, key = lambda item: len(item[0]), reverse = True)

        l = len(str101)+5
        print("DEC: {}".format(str101))
        print("ENC: {}".format(str102))
        print("-" * l)

        # brute force loop
        print("*************************")
        print("Attempting brute force...")
        print("*************************")
        return self.use_z_force(L100, str101, str102, msg)



        

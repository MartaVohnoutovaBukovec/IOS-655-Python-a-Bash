#!/usr/bin/env python3
#
# Subject: UAI / 655, Lecturer Ing. Marta Vohnoutová
# Homework No 13:
# Pattern list of candidates from dictionary separated by ',',
# e.g. '0.0.1.2.3' [‘AARON’, ‘LLOYD’, ‘OOZED’]
# sort them and print them to a file
#
# Author: Alexandre Lysov
# Date: April 21, 2017

def get_pattern(word):
    """ This function returns a letter pattern of a word.
    """
    temp = ""
    pattern = ""

    for c in word:
        if (c not in temp):
            temp += c
        pattern += str(temp.find(c)) + "."
            
    return pattern[:len(pattern)-1]

def main():
    
    patterns = dict()
    
    try:
        # 'with' block will automatically close files on exit from it
        with open("words_patterns.txt", "w") as wp:
            with open("en_words.txt") as words:
                for word in words:
                    word = word.strip()
                    if (len(word) > 0):
                        pattern = get_pattern(word)
                        patterns.setdefault(pattern, list()).append(word)

            for p in sorted(patterns):
                wp.write("'{0}' {1}\r\n".format(p, patterns[p]))

    except Exception as err:
        print(err)

main()



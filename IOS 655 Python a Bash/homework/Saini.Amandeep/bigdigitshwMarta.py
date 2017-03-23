import sys
import random

Zero = ["  ***  ",
         " *   * ",
         "*     *",
         "*     *",
         "*     *",
         " *   * ",
         "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ",
         "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
     digits = str(random.randint(0,99999999))
     row = 0
     while row < 7:
         line = ""
         column = 0
         while column < len(digits):
             number = int(digits[column])
             digit = Digits[number]
             line += digit[row] + "  "
             column += 1
         print(line)
         row += 1
except IndexError:
     print("usage: bigdigits.py <number>")
except ValueError as err:
     print(err, "in", digits)




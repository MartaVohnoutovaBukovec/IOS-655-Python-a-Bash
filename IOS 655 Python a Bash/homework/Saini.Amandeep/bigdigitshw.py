Last login: Thu Mar  9 18:38:27 on ttys000
Amandeeps-MacBook-Pro:~ AmanSaini$ python3
Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 08:49:46) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> 
>>> Zero = ["  ***  ",
...         " *   * ",
...         "*     *",
...         "*     *",
...         "*     *",
...         " *   * ",
...         "  ***  "]
>>> One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
>>> Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
>>> Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
>>> Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ",
...         "   *  "]
>>> Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
>>> Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
>>> Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
>>> Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
>>> Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
>>> 
>>> Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
>>> 
>>> try:
...     digits = '0123456789'
...     row = 0
...     while row < 7:
...         line = ""
...         column = 0
...         while column < len(digits):
...             number = int(digits[column])
...             digit = Digits[number]
...             line += digit[row] + "  "
...             column += 1
...         print(line)
...         row += 1
... except IndexError:
...     print("usage: bigdigits.py <number>")
... except ValueError as err:
...     print(err, "in", digits)
... 
  ***     *    ***    ***      *    *****   ***   *****   ***    ****  
 *   *   **   *   *  *   *    **    *      *          *  *   *  *   *  
*     *   *   *  *       *   * *    *      *         *   *   *  *   *  
*     *   *     *      **   *  *     ***   ****     *     ***    ****  
*     *   *    *         *  ******      *  *   *   *     *   *      *  
 *   *    *   *      *   *     *    *   *  *   *  *      *   *      *  
  ***    ***  *****   ***      *     ***    ***   *       ***       *  
>>> 




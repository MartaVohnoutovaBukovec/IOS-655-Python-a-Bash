#!/usr/bin/env python3

Zero = ["  ***  ", " *   * ", "*     *", "*     *", "*     *", " *   * ", "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]


number=str(input("Enter a random number: "))
while int(number) < 0:
        number=str(input("Please, enter only a positive number: "))

while int(number) > 1000:
        number=str(input("Please, enter a number smaller than 1000: "))        
digits=list(number)
for i in digits:
        if i == "0":
                for i in Zero:
                        print(i)
                pass
        elif i == "1":
                for i in One:
                        print(i)
                pass
        elif i == "2":
                for i in Two:
                        print(i)
                pass
        elif i == "3":
                for i in Three:
                        print(i)
                pass
        elif i == "4":
                for i in Four:
                        print(i)
                pass
        elif i == "5":
                for i in Five:
                        print(i)
                pass
        elif i == "6":
                for i in Six:
                        print(i)
                pass
        elif i == "7":
                for i in Seven:
                        print(i)
                pass
        elif i == "8":
                for i in Eight:
                        print(i)
                pass
        elif i == "9":
                for i in Nine:
                        print(i)
                pass
print("The number you chose was printed on the screen, now let's write a random number between 0-1000.")


import random

guessed = str(random.randint(0, 1000))
print("\nMy random number is:", guessed, "and it is written in bigdigits below...")
digits=list(guessed)
for i in digits:
        if i == "0":
                for i in Zero:
                        print(i)
                pass
        elif i == "1":
                for i in One:
                        print(i)
                pass
        elif i == "2":
                for i in Two:
                        print(i)
                pass
        elif i == "3":
                for i in Three:
                        print(i)
                pass
        elif i == "4":
                for i in Four:
                        print(i)
                pass
        elif i == "5":
                for i in Five:
                        print(i)
                pass
        elif i == "6":
                for i in Six:
                        print(i)
                pass
        elif i == "7":
                for i in Seven:
                        print(i)
                pass
        elif i == "8":
                for i in Eight:
                        print(i)
                pass
        elif i == "9":
                for i in Nine:
                        print(i)
                pass

print("The first excercize is completed!")



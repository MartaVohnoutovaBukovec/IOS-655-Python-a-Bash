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


number=str(input("Enter a positive number: "))
while int(number) < 0:
        number=str(input("Please, enter only a positive number: "))
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
print("Your number was printed on screen.")

# I have a doubt, I would like to know how to put all the big digits in the same line, so the printed result looks better.



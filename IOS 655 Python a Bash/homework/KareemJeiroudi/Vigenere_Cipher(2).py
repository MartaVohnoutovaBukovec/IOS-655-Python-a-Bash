def encryption(plaintext, keyword):
    # Do the operation once
    txt_len = len(plaintext)

    # Get a string just a bit longer than plaintext
    # Otherwise we would have issues when plaintext is n ot a multiple of keyword
    keyword *= txt_len // len(keyword) + 1  # // is floor division
    # Chop of the extra characters (if there are any)
    keyword = keyword[:txt_len]

    # Create a string to store the encrypted message
    encoded = ""

    # Now you should change this to work with capital letters
    for c in range(txt_len):
        # 194 = 2 * ord('a')
        newchar = ord(plaintext[c]) + ord(keyword[c]) - 194
        newchar %= 25
        encoded += chr(newchar + 97)  # 97 = ord('a')

    return encoded


def encrypt_input():
    # This function should use input to get plaintext and keyword
    # Then use encryption with those strings and print the result
    plaintext = input("Please enter your plaintext you wish to encode.")
    keyword = input("Please enter your keyword(subkeys), preferably shorter than the plaintext.")

    print(encryption(plaintext, keyword))
    pass

encrypt_input()

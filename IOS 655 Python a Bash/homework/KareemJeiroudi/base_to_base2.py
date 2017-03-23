def base_to_base(starting_base, string, ending_base):
    n = string_to_int(string, starting_base)
    return int_to_string(n, ending_base)

def string_to_int(string, base):
    num = 0
    for digit in string:
        if digit.isalpha():
            current_value = ord(digit) - 55
        else:
            current_value = int(digit)
        num = base * num + current_value
    return num

def int_to_string(n, base):
    if n==0:
        return "0"

    string = ""
    while n:
        n, current_value = divmod(n, base)
        if current_value > 9:
            current_value = chr(current_value + 55)
        else:
            current_value = str(current_value)
        string = current_value + string
    return string

def get_integer_in_range(prompt, mini, maxi):
    while True:
        starting_base = input(prompt)
        if starting_base.isdigit() and mini <= int(starting_base) <= maxi:
            return int(starting_base)
        print("Please enter a positive integer between %d and %d" % (mini, maxi))

def get_starting_num(starting_base):
    """ Input and verification of starting number, that it is a positive integer
    using only characters from its base. Returns starting_num as a string."""
    # Assigns string which only contains characters from the given base
    base_members = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:starting_base]

    while True:
        starting_num = input("starting number: ")
        if all(c in base_members for c in starting_num): 
            return starting_num
        print("Please only use characters in your base (Capital letters for " +
              "bases larger than than 10)")

if __name__ == "__main__":
    for s in ["0", "1", "4", "6", "10", "23", "7257"]:
        assert string_to_int(s, 10) == int(s)
    for n in [0, 1, 4, 6, 10, 23, 7257]:
        assert int_to_string(n, 10) == str(n)
    starting_base = get_integer_in_range("starting base: ", 2, 36)
    starting_num = get_starting_num(starting_base)
    ending_base = get_integer_in_range("ending base: ", 2, 36)
    ending_num = base_to_base(starting_base, starting_num, ending_base)
    print("ending number: " + ending_num)

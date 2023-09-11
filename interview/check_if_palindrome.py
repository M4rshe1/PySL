# check i two strings are palindromes

def check_if_is_palindrome(string):
    if string == string[::-1]:
        return "Is palindrome"
    else:
        return "Is not palindrome"


if __name__ == "__main__":
    input(check_if_is_palindrome(input("Word 1: ")))

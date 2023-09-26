import random
import string
import pyperclip


def check_for_numbers(input_string):
    return any(char.isdigit() for char in input_string)


def check_for_special_chars(input_string):
    return any(char in string.punctuation for char in input_string)


def check_for_uppercase(input_string):
    return any(char.isupper() for char in input_string)


def check_for_lowercase(input_string):
    return any(char.islower() for char in input_string)


def check_string(input_string):
    array_of_chars = []
    if len(input_string) < 1:
        exit("Error: String is empty.")
    if check_for_lowercase(input_string):
        array_of_chars.append(string.ascii_lowercase)
    if check_for_uppercase(input_string):
        array_of_chars.append(string.ascii_uppercase)
    if check_for_numbers(input_string):
        array_of_chars.append(string.digits)
    if check_for_special_chars(input_string):
        array_of_chars.append(string.punctuation)
    if len(array_of_chars) < 1:
        exit("Error: No valid characters.")
    return "".join(array_of_chars)


def generate_random_string(array_of_chars, length=16):
    # print(array_of_chars)
    gen_string = ""
    for i in range(length):
        gen_string += random.choice(array_of_chars)
    with open("random_string.txt", "a") as f:
        new_line = "\n" if f.tell() != 0 else ""
        f.write(f"{new_line}{gen_string}")
    return gen_string


if __name__ == "__main__":
    array_of_selected_char = check_string(
        input("Write a string with all the symbol types you want to use (lower, upper, numbers and special)\n>> "))
    length_of_string = input("Write the length of the string\n>> ")
    if not length_of_string.isnumeric():
        length_of_string = len(length_of_string)

    random_string = generate_random_string(array_of_selected_char, int(length_of_string))
    pyperclip.copy(random_string)
    print("String copied to clipboard")
    input(f"Random string generated: {random_string}\nPress ENTER to exit")



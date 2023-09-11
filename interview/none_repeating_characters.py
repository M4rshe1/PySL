# Find none repeating characters in a string

def none_repeating_characters(string):
    for i in string:

        count = 0

        for j in string:
            if i == j:
                count += 1

            if count > 1:
                break

        if count == 1:
            print(i)


print(none_repeating_characters(input("Enter a string: ")), end="")
input()

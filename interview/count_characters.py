# Script to count the number the frequency of characters in a string

def count_characters(string):
    # remove all spaces from the string
    string = string.replace(" ", "").lower()
    # split the string into characters
    characters = list(string)
    # create a dictionary to store the characters and their frequency
    character_frequency = {}
    # loop through the characters
    for character in characters:
        # if the character is already in the dictionary, increment its frequency
        if character in character_frequency:
            character_frequency[character] += 1
        # if the character is not in the dictionary, add it to the dictionary
        else:
            character_frequency[character] = 1
    # sort the dictionary by the frequency of the characters
    character_frequency = sorted(character_frequency.items(), key=lambda x: x[1], reverse=True)
    # return the dictionary
    return character_frequency


input(count_characters(input("Enter a string: ")))

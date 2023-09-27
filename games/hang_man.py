import random
import string

wordlist_de = "./wordlist_de.txt"
wordlist_en = "./wordlist_en.txt"


def get_word():
    with open(wordlist, 'r') as f:
        words = f.readlines()

    return random.choice(words).strip()


def print_word(word, guesses):
    guessed_word = ""
    for letter in word:
        if letter.lower() in guesses or letter.upper() in guesses:
            guessed_word += letter
            print(letter + " ", end="")
        else:
            print("_ ", end="")
    print("\n")
    return guessed_word


def print_man(guesses, word):
    if guesses == 1:
        print("_|_")
    elif guesses == 2:
        print(" | \n | \n_|_ ")
    elif guesses == 3:
        print(" | \n | \n | \n | \n_|_ ")
    elif guesses == 4:
        print("  ___\n | \n | \n | \n | \n | \n_|_ ")
    elif guesses == 5:
        print("  ___\n |   |\n | \n | \n | \n | \n_|_ ")
    elif guesses == 6:
        print("  ___\n |   |\n |   O\n |   |\n | \n | \n_|_ ")
    elif guesses == 7:
        print("  ___\n |   |\n |   O\n |  /|\\\n |   |\n | \n_|_")
    elif guesses == 8:
        print("  ___\n |   |\n |   O\n |  /|\\\n |   |\n |  / \\\n_|_")
        print("Loser")
        print("The word was: " + word)
        return True
    return False


if __name__ == "__main__":
    while True:
        language = input("Choose language (de/en): \n>> ")
        if language == "de":
            wordlist = wordlist_de
            break
        elif language == "en":
            wordlist = wordlist_en
            break
    word_to_guess = get_word()
    wrong_guesses = 0
    guessed_letters = []
    while True:
        print("\n" * 100)
        if print_man(wrong_guesses, word_to_guess):
            break
        word_guessed = print_word(word_to_guess, guessed_letters)
        print("Guessed letters: " + str(guessed_letters))
        guess = input("Guess a letter: \n>> ").lower()
        if guess in guessed_letters or guess not in string.ascii_lowercase or len(guess) != 1:
            print("NOT VALID or ALREADY GUESSED")
            continue
        elif guess in word_to_guess.lower():
            print("Correct!")
            guessed_letters.append(guess)
            word_guessed = print_word(word_to_guess, guessed_letters)
            if word_guessed == word_to_guess:
                print("You win!")
                break
        else:
            print("Incorrect!")
            wrong_guesses += 1
            guessed_letters.append(guess)
        guessed_letters.sort()

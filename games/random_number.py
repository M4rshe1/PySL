import random

# --- Random number game ---
# The game is played with one player.
# The player has to guess a number between one and the highest number.
# The player has to guess the number in the least number of guesses.
# --- Random number game ---


if __name__ == "__main__":
    guesses = 0
    while True:
        try:
            user_input = int(input("Enter the highest number: "))
            break
        except ValueError:
            print("Invalid input!")
            continue
    random_number = random.randint(1, user_input)
    while True:
        try:
            user_input = int(input("Enter a number: "))
            guesses += 1
            if user_input == random_number:
                input("You guessed it!\n It took you " + str(guesses) + " guesses!")
                break
            elif user_input > random_number:
                print("Too high!")
                continue
            elif user_input < random_number:
                print("Too low!")
                continue
        except ValueError:
            print("Invalid input!")

import random
player = 0
computer = 0

while True:
    print("Welcome to the game of Stone, Paper and Scissors")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")
    user_choice = int(input("Enter your choice: "))
    if user_choice == 1:
        print("You have selected Stone")
    elif user_choice == 2:
        print("You have selected Paper")
    elif user_choice == 3:
        print("You have selected Scissors")
    elif user_choice == 4:
        print("Thanks for playing the game")
        break
    else:
        print("Invalid choice")
        continue

    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        print("Computer has selected Stone")
    elif computer_choice == 2:
        print("Computer has selected Paper")
    elif computer_choice == 3:
        print("Computer has selected Scissors")
    if user_choice == computer_choice:
        print("Match is draw")
    elif (
            user_choice == 1 and computer_choice == 2
            or user_choice == 2 and computer_choice == 1
            or user_choice == 3 and computer_choice == 1
    ):
        player += 1
        print("Computer has won the match")
    elif (
            user_choice == 1 and computer_choice == 3
            or user_choice == 2 and computer_choice == 1
            or user_choice == 3 and computer_choice == 2
    ):
        computer += 1
        print("You have won the match")
    print("Player: ", player)
    print("Computer: ", computer)
    print()
    print()

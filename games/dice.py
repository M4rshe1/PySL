import random


# --- Dice game ---
# The game is played with 2 - 4 players.
# The fist player to reach 100 points wins!
# # If you roll a 1, your turn is over, and you lose all the points you rolled in that turn.
# If you roll a 2 - 6, you can either roll again or give it to the next player.
# If you give it to the next player, you keep the points you rolled in that turn.
# --- Dice game ---


def dice():
    return random.randint(1, 6)


if __name__ == "__main__":
    while True:
        players = input("How many players? (2 - 4) \n>> ")
        if players.isdigit():
            players = int(players)
            if players in range(2, 5):
                break
            else:
                print("Invalid input!")
                continue
        else:
            print("Invalid input!")
            continue
    player_scores = [0 for _ in range(players)]
    while True:
        for i in range(players):
            temp_score = 0
            while True:
                print(f"Player {i + 1} is on turn!")
                if input("Press Enter to roll or give it to the next player with (n): ") != "n":
                    roll = dice()
                    if roll == 1:
                        print("You rolled 1, your turn is over!")
                        break
                    temp_score += roll
                    print(f"Your current score is {temp_score}")
                    if player_scores[i] + temp_score >= 100:
                        input(f"Player {i + 1} wins!")
                        for j in range(players):
                            print(f"Player {j + 1} has {player_scores[j]} points!")
                        exit()
                else:
                    player_scores[i] += temp_score
                    print(f"Player {i + 1} has the {player_scores[i]} total points!")
                    break


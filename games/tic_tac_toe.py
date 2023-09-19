import os

# ------------------- Tic Tac Toe -------------------
# The game is played with two players
# The players take turns placing their mark on the game field.
# The first player to get 3 in a row wins!
# If all the fields are filled and no one has 3 in a row, it's a draw!
# ------------------- Tic Tac Toe -------------------


possible_moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
all_moves = {'a1': ' ', 'a2': ' ', 'a3': ' ', 'b1': ' ', 'b2': ' ', 'b3': ' ', 'c1': ' ', 'c2': ' ', 'c3': ' '}
int_moves = {'a1': 'X', 'a2': 'O', 'a3': ' ', 'b1': ' ', 'b2': 'X', 'b3': ' ', 'c1': ' ', 'c2': 'O', 'c3': 'X'}


def print_game_field(moves):
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n       1         2         3     ")
    print('')
    print("            |         |          ")
    print(f"a      {moves['a1']}    |    {moves['a2']}    |    {moves['a3']}     ")
    print("            |         |          ")
    print('   ---------|---------|----------')
    print("            |         |          ")
    print(f"b      {moves['b1']}    |    {moves['b2']}    |    {moves['b3']}     ")
    print("            |         |          ")
    print('   ---------|---------|----------')
    print("            |         |          ")
    print(f"c      {moves['c1']}    |    {moves['c2']}    |    {moves['c3']}     ")
    print("            |         |          ")
    print('\n\n')


def check_win():
    if all_moves['a1'] == all_moves['a2'] == all_moves['a3'] != ' ':
        input(f"{all_moves['a1']} wins!")
        return True
    elif all_moves['b1'] == all_moves['b2'] == all_moves['b3'] != ' ':
        input(f"{all_moves['b1']} wins!")
        return True
    elif all_moves['c1'] == all_moves['c2'] == all_moves['c3'] != ' ':
        input(f"{all_moves['c1']} wins!")
        return True
    elif all_moves['a1'] == all_moves['b1'] == all_moves['c1'] != ' ':
        input(f"{all_moves['a1']} wins!")
        return True
    elif all_moves['a2'] == all_moves['b2'] == all_moves['c2'] != ' ':
        input(f"{all_moves['a2']} wins!")
        return True
    elif all_moves['a3'] == all_moves['b3'] == all_moves['c3'] != ' ':
        input(f"{all_moves['a3']} wins!")
        return True
    elif all_moves['a1'] == all_moves['b2'] == all_moves['c3'] != ' ':
        input(f"{all_moves['a1']} wins!")
        return True
    elif all_moves['a3'] == all_moves['b2'] == all_moves['c1'] != ' ':
        input(f"{all_moves['a3']} wins!")
        return True
    elif all_moves['a1'] != ' ' and all_moves['a2'] != ' ' and all_moves['a3'] != ' ' and all_moves['b1'] != ' ' and \
            all_moves['b2'] != ' ' and all_moves['b3'] != ' ' and all_moves['c1'] != ' ' and \
            all_moves['c2'] != ' ' and all_moves['c3'] != ' ':
        input("Draw!")
        return False


if __name__ == '__main__':
    print_game_field(int_moves)
    print("Welcome to \n")
    print("T I C - T A C - T O E\n")
    print("G A M E !\n")
    input("Press enter to start the game!")
    print_game_field(all_moves)
    while True:
        while True:
            print("Please enter in this format: a1, b2, c3, etc.")
            player_input = input("X is on turn: \n>> ")
            if player_input in possible_moves:
                if all_moves[player_input] != ' ':
                    print("This field is already taken, try again")
                    continue
                all_moves[player_input] = 'X'
                break
            else:
                print("Invalid input!, try again")
                continue
        print_game_field(all_moves)
        if check_win():
            break
        while True:
            print("Please enter in this format: a1, b2, c3, etc.")
            player_input = input("O is on turn: \n>> ")
            if player_input in possible_moves:
                if all_moves[player_input] != ' ':
                    print("This field is already taken, try again")
                    continue
                all_moves[player_input] = 'O'
                break
            else:
                print("Invalid input!, try again")
                continue
        if check_win():
            break

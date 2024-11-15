# Snakes and ladders program

# -------------------------
# Import libraries
# -------------------------
import random


# -------------------------
# Subprograms
# -------------------------
def play(board, players):
    current_player = 0
    game_won = False
    while not game_won:
        player_square = players[current_player]
        print()
        print("------------------------------------")
        print("Player", current_player + 1, "it's your turn.")
        print("You are on square", player_square)
        print("Press Enter to roll the dice.")
        wait = input()
        dice = random.randint(1, 6)
        print("You rolled a", dice)
        player_square = player_square + dice
        if player_square > len(board) - 1:
            player_square = len(board) - 1
        print("You moved to square", player_square)
        board_square = board[player_square]
        if  board_square < player_square:
            print("Oh no, you landed on a snake.")
            player_square = board_square
            print("You are now on square", player_square)
        elif board_square > player_square:
            print("Yay, you landed on a ladder.")
            player_square = board_square
            print("You are now on square", player_square)
        if player_square >= len(board) - 1:
            game_won = True
            print("Player", current_player + 1, "wins the game!")
        else:
            players[current_player] = player_square
            print("Press Enter for the next player to take their turn.")
            wait = input()
            current_player = (current_player + 1) % len(players)


def initialise_board(squares, num_specials):
    random.seed()
    board = []
    specials = []
    for square in range(squares + 1):
        board.append(square)
    for special in range(0,num_specials):
        square = random.randint(2,24)
        while square in specials:
            square = random.randint(2,24)
        board[square] = random.randint(2,24)
        while board[square] in specials or board[square] == square:
            board[square] = random.randint(2,24)
        specials.append(square)

    return board


def initialise_players():
    players = [1]*int(input("How many players?: "))
    return players


# -------------------------
# Main program
# -------------------------
board = initialise_board(25, 5)
players = initialise_players()
play(board, players)

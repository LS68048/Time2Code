# Noughts and crosses program

# -------------------------
# Subprograms
# -------------------------

def get_move(turn):
    pos = input("Enter the XY coordinates of the square you want to place: ")
    x = int(pos[0])
    y = int(pos[1])
    valid = False
    while not valid:
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Invalid square.")
        if board[x][y] != -1:
            print("Invalid square.")
        else:
            valid = True
            continue
        pos = input("Enter the XY coordinates of the square you want to place: ")
        x = int(pos[0])
        y = int(pos[1])
    board[x][y] = turn

def draw_board():
    layout = "{:^3}{:<2}{:<3}"
    print(layout.format("0","1","2"))
    rowcount = 0
    for row in board:
        rowtext = str(rowcount)
        for item in row:
            if item == -1:
                rowtext += " "
            elif item == 0:
                rowtext += "O"
            else:
                rowtext += "X"
            rowtext += "|"
        rowcount += 1
        print("-"*9)
        print(rowtext[:len(rowtext)-1])

def won():
    htotal = 0
    vtotal = 0
    for i in range(3):
        for j in range(3):
            htotal += board[i][j]
            vtotal += board[j][i]
        if htotal == 30 or htotal == 0 or vtotal == 30 or vtotal == 0:
            return True
        htotal = 0
        vtotal = 0
    dtotal = board[0][0] + board[1][1] + board[2][2]
    if dtotal == 30 or dtotal == 0:
        return True
    dtotal = board[2][0] + board[1][1] + board[0][2]
    if dtotal == 30 or dtotal == 0:
        return True
    return False

def play_game():
    turn = 10
    remaining = 9
    winner = ""
    while remaining > 0:
        draw_board()
        get_move(turn)
        if won():
            remaining = 0
            winner = "X" if turn == 10 else "O"
        elif turn == 10:
            turn = 0
        else:
            turn = 10
        remaining -= 1
    print("DRAW!" if winner == "" else winner + " wins!")

# -------------------------
# Main program
# -------------------------

board = [[-1 for i in range(3)] for j in range(3)]
play_game()

# Your move program

# -------------------------
# Subprograms
# -------------------------
def get_move():
    move = input("Enter your move: ")
    move.strip()
    move = move.upper()
    return move

def get_indexes(move):
    coords = []
    coords.append(move[0])
    coords.append(int(move[1]))

    coords[0] = ord(coords[0])-64

    return coords

# -------------------------
# Main program
# -------------------------
move = get_move()
print(get_indexes(move))

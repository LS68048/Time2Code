# Word game program

# -------------------------
# Import libraries
# -------------------------
import random


# -------------------------
# Subprograms
# -------------------------
def shuffle_letters():
        grid = [["" for column in range(4)] for row in range(4)]
        file = open("dice.txt", "r")
        i = 0
        j = 0
        for line in file.readlines():
                letters = line.strip().split(",")
                grid[i][j] = letters[random.randint(0,4)]
                j += 1
                if j >= 4:
                        i += 1
                        j = 0
        return grid

def show_letters(grid):
        for i in range(0,4):
                print(grid[i][0], grid[i][1], grid[i][2], grid[i][3])
        

# -------------------------
# Main program
# -------------------------
grid = shuffle_letters()
show_letters(grid)

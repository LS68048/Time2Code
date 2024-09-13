# Polyhedral dice program

# -------------------------
# Import libraries
# -------------------------
import random


# -------------------------
# Subprograms
# -------------------------
def roll_dice(sides):
    return random.randint(1, sides)


# -------------------------
# Main program
# -------------------------

sides = int(input("Roll a D"))
random.seed()
number = roll_dice(sides)
if number == 8 or number == 11:
    print("You rolled an", number)
else:
    print("You rolled a", number)

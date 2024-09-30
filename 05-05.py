# Cup draw program

# -------------------------
# Import libraries
# -------------------------
import random


# -------------------------
# Subprograms
# -------------------------
def input_teams():
    more = "y"

    while more != "n":
        teams.append(input("Enter the name of a team: "))
        teams.append(input("Enter the name of a team: "))
        more = input("add two more teams? y/n : ")
        while more not in ["y","n"]:
            more = input("add two more teams? y/n : ")

def draw_teams():
    random.shuffle(teams)
    print("The draw is:")
    while len(teams) > 0:
        print(teams.pop(),"v",teams.pop())
        
# -------------------------
# Main program
# -------------------------

teams = []
input_teams()
draw_teams()
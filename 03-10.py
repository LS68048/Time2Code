# Fox, chicken, grain program

# Subprograms

def output():
    this_side = []
    that_side = []
    for item in ["fox", "chicken", "grain", "farmer"]:
        if eval(item) == 0:
            this_side.append(item)
        else:
            that_side.append(item)
    
    print("This side of the river:")
    for item in this_side:
        print(item)
    
    print("\nThe other side of the river:")
    for item in that_side:
        print(item)

def wrong_move():
    if fox != farmer and chicken != farmer:
        print("The fox ate the chicken")
        return True
    elif chicken != farmer and grain != farmer:
        print("The chicken ate the grain")
        return True
    return False

def puzzle_solved():
    if fox == 1 and chicken == 1 and grain == 1:
        print("You solved the puzzle!")
        return True
    else:
        return False

# Main Program
print("A fox, chicken and a bag of grain wait by the side of a river.")
fox = chicken = grain = farmer = 0

win = False
lose = False

while not (win or lose):
    choice = input("Which item will you take in your rowboat to the other side?\nfox, chicken, grain or farmer?\nChoose: ")

    if choice == "farmer":
        farmer = not farmer
    elif choice == "fox" and not (fox or farmer):
        fox = farmer = 1
    elif choice == "grain" and not (grain or farmer):
        grain = farmer = 1
    elif choice == "chicken" and not (chicken or farmer):
        chicken = farmer = 1

    elif choice == "fox" and (farmer and fox):
        fox = farmer = 0
    elif choice == "chicken" and (farmer and chicken):
        chicken = farmer = 0
    elif choice == "grain" and (farmer and grain):
        grain = farmer = 0

    print("-"*10)
    output()
    print("-"*10)

    lose = wrong_move()

    win = puzzle_solved()
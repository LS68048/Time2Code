# Attributes program

# -------------------------
# Subprograms
# -------------------------
def make_character():
    name = input("Enter the name of the character: ")
    health = int(input("Enter the health: "))
    attack = int(input("Enter the attack: "))
    defend = int(input("Enter the defend"))
    return [name,health,defend,attack]

def save_character(attributes):
    file = open(attributes[0]+".txt","w")
    file.write("[Name]\n"+attributes[0])
    file.write("[Attributes]")
    file.write(attributes[1])
    file.write(attributes[2])
    file.write(attributes[3])
    file.close()


# -------------------------
# Main program
# -------------------------
character = make_character()
save_character(character)
print("Character saved.")

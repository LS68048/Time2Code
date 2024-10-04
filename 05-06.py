# Feud program

# -------------------------
# Subprograms
# -------------------------
def forage_herb():
    herb = input("What herb do you want to look for?: ")
    if herb in ["dandelion", "burdock", "pipewort", "ragwort", "snapdragon", "toadflex"]:
        print(herb,"found!")
        herbs_collected.append(herb)
    else:
        print("Connot find herb.")


def cauldron(spell, herb):
    try:
        index1 = herbs_collected.index(herb[0])
        del herbs_collected[index1]
        
        index2 = herbs_collected.index(herb[1])
        del herbs_collected[index2]

        spells_brewed.append(spell)
        print(f"{spell} has been brewed.")
        
    except(ValueError):
        print("Cannot brew the spell, you don't have the correct herbs.")
    


def brew_spell():
    spell = input("What spell do you want to brew?: ")
    try:
        herb = herbs_required[spell]
        cauldron(spell, herb)
    except(KeyError):
        print("That spell is not in the spell book")
        
def cast_spell():
    spell = input("What spell do you want to cast?: ")
    if spell in spells_brewed:
        del spells_brewed[spells_brewed.index(spell)]
        print(spell, "has been cast")
    else:
        print("You have not brewed that spell.")

def take_action():
    option = input("Forage herb, brew or cast a spell? (f/b/c): ")
    while option not in ["f","b","c"]:
        option = input("Forage herb, brew or cast a spell? (f/b/c): ")
    if option == "f":
        forage_herb()
    elif option == "b":
        brew_spell()
    elif option == "c":
        cast_spell()


# -------------------------
# Main program
# -------------------------

herbs_collected = []
herbs_required = {
    "teleport":["dandelion", "burdock"],
    "protect":["pipewort","ragwort"],
    "sprites":["snapdragon","toadflex"]
}
spells_brewed = []

while True:
    take_action()

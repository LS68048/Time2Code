# Search for life program

# -------------------------
# Import libraries
# -------------------------
import random


# -------------------------
# Subprograms
# -------------------------
def probe(planet):    
    creature = ["lizards", "humanoids", "insects"]
    colour = ["red", "green", "blue"]
    characteristic = ["shy", "angry", "docile"]
    climate = ["hot", "frozen", "barren", "temperate"]
    
    random.seed(planet)
    lifeform = random.randint(0,2)
    specimen = random.randint(0,2)
    behaviour = random.randint(0,2)
    temperature = random.randint(0,3)
    
    report = ""
    if temperature == 3:
        report = colour[specimen]
        report = report + ", " + characteristic[behaviour]
        report = report + " " + creature[lifeform]
        report = report + " on the planet."
    else:
        report = "a " + climate[temperature] + " planet with no signs of life"
    return report
    
    
# -------------------------
# Main program
# -------------------------
planet = int(input("Enter the catalogue number of a planet: "))
report = probe(planet)
print("Probes report", report)

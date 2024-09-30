# Random name generator program

# -------------------------
# Import libraries
# -------------------------
import random


# -------------------------
# Subprograms
# -------------------------
# Function to return a random name
def generate_name():
    forenames = ["Muhammad", "Noah", "Jack", "Lily", "Sophia", "Olivia"]
    surnames = ["Wang", "Smith", "Devi", "Jones", "Kim", "Rodríguez"]
    return forenames[random.randint(0,len(forenames)-1)] + " " + surnames[random.randint(0,len(surnames)-1)]

# -------------------------
# Main program
# -------------------------

print(generate_name())

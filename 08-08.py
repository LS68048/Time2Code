# Amino acids program

# -------------------------
# Subprograms
# -------------------------
def get_amino_acid():
    valid = False
    acid = ""
    while not valid:
        acid = input("Enter the amino acid to find: ")
        valid = True
        if len(acid) < 3 or len(acid) > 3:
            valid = False
        else:
            for letter in acid:
                if letter not in ["A","C","G","T"]:
                    valid = False
    return acid
    
def check_sequence(acid):
    try:
        file = open("dna.txt","r")
        count = 0
        for line in file.readlines():
            for index in range(0,len(line)-1,3):
                currentAcid = line[index] + line[index+1] + line[index+2]
                if currentAcid == acid:
                    count += 1
        file.close()
        return count
    except FileNotFoundError:
        return -1

# -------------------------
# Main program
# -------------------------

acid = get_amino_acid()
acids = check_sequence(acid)
if acids == -1:
    print("DNA file not found.")
else:
    print(f"There are {acids} {acid} acids in the DNA sequence")

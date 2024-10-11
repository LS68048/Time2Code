# Find and replace program

# -------------------------
# Subprograms
# -------------------------
def replace(x, y, l):
    for word in l:
        if word == x:
            l[l.index(word)] = y
    return l


def output(l):
    for word in l:
        print(word)
        
        
# -------------------------
# Main program
# -------------------------
rhyme = ["roly", "poly", "roly", "poly", "up", "up", "up", 
         "roly", "poly", "roly", "poly", "down", "down", "down"]

output(rhyme)

replaced = input("Which word to replace?: ")
replacer = input("Replace with what?: ")
new_rhyme = replace(replaced,replacer,rhyme)
output(new_rhyme)
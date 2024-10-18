# Saving data program

# -------------------------
# Subprograms
# -------------------------
def load(filename):
    file = open(filename, "r")
    user = file.read()
    file.close()
    user = user.strip()
    return user


def save(user, filename):
    file = open(filename, "w")
    user = user + "\n"
    file.write(user)
    file.close()


# -------------------------
# Main program
# -------------------------
filename = "datafile.txt"
try:
    user = load(filename)
    print("It's good to see you again,", user + ".")
except FileNotFoundError:
    name = input("Hello, I don't believe we have met.\nWhat is your name?: ")
    save(name,filename)
    print("Nice to meet you",name)

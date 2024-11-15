# Gamertag program

# -------------------------
# Subprograms
# -------------------------
def check_exists(tag):
    try:
        file = open("players.txt","r")
        for line in file.readlines():
            if line == tag + "\n":
                file.close()
                return True
        file.close()
        return False
    except FileNotFoundError:
        file = open("players.txt","w")
        file.close()
        return False

def write_gamertag(tag):
    file = open("players.txt", "a")
    file.write(tag+"\n")
    file.close()

def get_gamertag():
    tag = input("Enter your unique gamertag: ")
    while check_exists(tag):
        print("Sorry, that gamertag is already taken. Try again.")
        tag = input("Enter your unique gamertag: ")
    write_gamertag(tag)
    print("Welcome",tag)

# -------------------------
# Main program
# -------------------------

get_gamertag()
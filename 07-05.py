# Disemvowel program

# -------------------------
# Subprograms
# -------------------------
def dvowel(message):
    for vowel in ["a","A","e","E","i","I","o","O","u","U"]:
        message = message.replace(vowel, "")
    return message

# -------------------------
# Main program
# -------------------------

message = input("Enter the message: ")
print(dvowel(message))
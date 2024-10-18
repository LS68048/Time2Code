# Palindrome program

# -------------------------
# Subprograms
# -------------------------
def palindrome(phrase):
    phrase = phrase.lower()
    backwards = []
    forwards = ""
    asList = []
    for char in phrase:
        asList.append(char)
    count = len(asList)-1
    for i in range(0,len(asList)):
        if asList[i].isalpha() and asList[i] != " ":
            forwards += asList[i]
            backwards.insert(0,asList[i])
        count -= 1
    return True if "".join(backwards) == forwards else False

# -------------------------
# Main program
# -------------------------

phrase = input("Enter a phrase: ")
print(phrase,"is","a" if palindrome(phrase) else "not a", "palindrome")

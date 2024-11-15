# Journey log program

# -------------------------
# Subprograms
# -------------------------
def add_chapter():
    book.append([])


def add_story(chapter, entry):
    book[chapter].append(entry)


def output():
    log = 1
    for chapter in range(1, len(book)):
        print("CHAPTER",chapter,"\n---------\n")
        for entry in book[chapter]:
            print("Log", log, ":", entry)
            log = log + 1
    
    
# -------------------------
# Main program
# -------------------------
book = [[]]
add_chapter()
add_story(1, "I find myself alone on a strange world, unequipped and in danger. I have no memory of how I got here, no sense of a before.")
add_story(1, "My Exosuit at least seems to know what it's doing, and I am not dead yet...")
add_chapter()
add_story(2, "I received a set of mysterious coordinates from an unknown source.")
add_story(2, "I followed the signal, and found the wreckage of an abandoned starship.")
add_story(2, "There was little to be gained from the wreck, but the distress beacon contained the hailing frequency labelled 'ARTEMIS'.")
output()
file = open("log.txt","w")
for line in book:
    if line != []:
        for story in line:
            file.write(story + "\n")
file.close()

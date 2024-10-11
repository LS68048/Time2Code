# Notebook program

# -------------------------
# Subprograms
# -------------------------
def get_note_number():
    valid_input = False
    while not valid_input:
        note_number = int(input("Note number: "))
        if note_number >= 0 and note_number < 10:
            valid_input = True
        else:
            print("Invalid input. Enter 0-9.")
    return note_number


def add_note():
    index = get_note_number()
    note = input("Enter the note: ")
    notebook[index] = note


def clear_notes():
    choice = ""
    while choice not in ["y", "n"]:
        choice = input("Are you sure you want to delete all notes? y/n :")
    if choice == "y":
        for index in range(len(notebook)):
            notebook[index] = ""


def order_notes():
    notebook.sort()

def delete_note():
    index = get_note_number()
    notebook [index] = ""

def move_notes():
    note1 = get_note_number()
    note2 = get_note_number()

    notebook[note1], notebook[note2] = notebook[note2], notebook[note1]

def show_notebook():
    for index in range(len(notebook)):
        print(index, ":", notebook[index])


def menu():
    print()
    print("a. Add note")
    print("c. Clear notebook")
    print("o. Order notes")
    print("d. Delete note")
    print("s. Swap notes")
    choice = input(":")
    
    match choice:
        case "a":
            add_note()
        case "c":
            clear_notes()
        case "o":
            order_notes()
        case "d":
            delete_note()
        case "s":
            move_notes()
        
            
# -------------------------
# Main program
# -------------------------
notebook = ["" for note in range(10)]
while True:
    show_notebook()
    menu()

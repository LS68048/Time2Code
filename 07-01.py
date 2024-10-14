# Debit card program

# -------------------------
# Subprograms
# -------------------------
def validate_number(number_on_card):
    valid = True
    number_of_characters = len(number_on_card)
    if number_of_characters == 16 or number_of_characters == 19:
        for character in number_on_card:
            if not character.isdigit() and character != " ":
                valid = False    
    else:
        valid = False
    return valid

def validate_name(string):
    for character in string:
        if not character.isalpha() and character != " ":
            return False
    print(string.upper())
    return True

def input_card_details():
    valid_name = False
    while not valid_name:
        string_input = input("Enter the name on the card: ")
        valid_name = validate_name(string_input)

    valid_card = False
    while not valid_card:
        number_input = input("Enter the 16 digit number: ")
        valid_card = validate_number(number_input)


# -------------------------
# Main program
# -------------------------
input_card_details()
print("Card details valid.")

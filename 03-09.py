# Measurements program

# -------------------------
# Subprograms
# -------------------------
def feet_to_inches(feet):
    return feet*12

def inches_to_feet(inches):
    return inches/12

def menu():
    choice = int(input("1. Feet to inches\n2. Inches to feet\n3. Quit\nEnter choice: "))
    while choice not in [1,2,3]:
        choice = int(input("1. Feet to inches\n2. Inches to feet\n3. Quit\nEnter choice: "))
    return choice

def converter():
    choice = menu()
    if choice == 3:
        print("Goodbye")
    elif choice == 2:
        inches = float(input("Enter the number of inches: "))
        print(f"{inches} inches is {inches_to_feet(inches)} feet")
    elif choice == 1:
        feet = float(input("Enter the number of feet: "))
        print(f"{feet} feet is {feet_to_inches(feet)} inches")

# -------------------------
# Main program
# -------------------------

converter()
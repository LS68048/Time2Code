# Cashpoint program

# -------------------------
# Subprograms
# -------------------------
def dispense(amount):
    print("W" + str(amount))
    out = 0
    while out <= amount-5:
        if amount-out >= 20:
            print("D20")
            out += 20
        elif amount-out >= 10:
            print("D10")
            out += 10
        elif amount-out >= 5:
            print("D5")
            out += 5

# -------------------------
# Main program
# -------------------------

amount = int(input("Enter the amount to withdraw: "))
dispense(amount)

# Valid month program

# -------------------------
# Subprograms
# -------------------------
def validate_month(month):
    if month >= 1 and month <= 12:
        return True
    else:
        return False

# -------------------------
# Main program
# -------------------------

month = int(input("Enter a month 1-12: "))
valid_month = validate_month(month)
while not valid_month:
    month = int(input("Enter a month 1-12: "))
    valid_month = validate_month(month)
print("Thank you. Input accepted.")
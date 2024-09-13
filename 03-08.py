# PIN program

# -------------------------
# Subprograms
# -------------------------
def get_pin():
    attempt = 1
    guess = int(input("Enter PIN: "))
    while attempt < 3 and guess != 7528:
        guess = int(input("Enter PIN: "))
        attempt += 1
    if guess != 7528:
        return False
    else:
        return True
    

# -------------------------
# Main program
# -------------------------

login = get_pin()
if login:
    print("Security check passed")
else:
    print("Locked out.")
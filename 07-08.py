# Email program

# -------------------------
# Subprograms
# -------------------------
def validate(email_address):
    if not "@" in email_address:
        return False
    user = email_address.split("@")[0]
    domain = email_address.split("@")[1]

    if not user.isalpha():
        if user.endswith(".") or user.endswith("-") or user.endswith("_"):
            return False
    elif not domain.isalnum():
        TLD = domain.split(".")[1]
        if len(TLD) < 3:
            return False
        if not "-" in domain:
            return False
    return True

# -------------------------
# Main program
# -------------------------

email_address = input("Enter your email address: ")
print("Your email address is","valid" if validate(email_address) else "invalid")
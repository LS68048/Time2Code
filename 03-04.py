# Exam grade program

# -------------------------
# Subprograms
# -------------------------
def compound(curr, interest, target):
    while curr < target:
        year = 1
        curr *= 1+interest/100
        print(f"Year {year}: Balance £{curr}")
        year += 1


# -------------------------
# Main program
# -------------------------
bal = int(input("Enter the balance to the nearest pound: "))
interest = int(input("Enter the % interest rate: "))
target = int(input("Enter the target balance to the nearest pound: "))

compound(bal, interest, target)
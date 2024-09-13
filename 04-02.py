# Save the change program

# -------------------------
# Subprograms
# -------------------------
def nearest_pound(amount):
    return int(amount) + 1


def save_the_change(amount):
    if int(amount) != amount:
        savings = nearest_pound(amount) - amount
    else:
        savings = 1
    return savings
    
    
# -------------------------
# Main program
# -------------------------
purchase_price = float(input("Enter the purchase price: £"))
debit = nearest_pound(purchase_price)
savings = save_the_change(purchase_price)
if int(purchase_price) == purchase_price:
    debit -= 1
    savings -= 1
print("Debit - £{0:.2f}".format(debit))
print("Credit to savings - £{0:.2f}".format(savings))

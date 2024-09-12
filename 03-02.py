# Car value program

# -------------------------
# Subprograms
# -------------------------
def show_value(value, resale_value):
    year = 0
    depreciation = 0.25
    while value >= resale_value and resale_value > 0 and year < 5:
        print("In year", year, "the car is worth £", value)
        value = int(value - (value * depreciation))
        year = year + 1
    print("Part exchange before the end of year", year)
    
    
# -------------------------
# Main program
# -------------------------
value = int(input("Enter the value of the car purchased: £"))
resale_value = int(input("Enter the minimum part exchange value: £"))
show_value(value, resale_value)

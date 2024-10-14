# Airline ticket program

# -------------------------
# Subprograms
# -------------------------
# Function to return truncated airport names
def airports(departure, arrival):
    return departure.upper()[:4]+"-"+arrival.upper()[:4]

# -------------------------
# Main program
# -------------------------
airport1 = input("Enter the name of the first airport: ")
airport2 = input("Enter the name of the second airport: ")
print(airports(airport1, airport2))

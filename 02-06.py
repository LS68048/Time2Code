# Currency converter program

# -------------------------
# Subprograms
# -------------------------
def exchange(gbp, currency):
  match currency:
    case "usd":
      return 1.3*gbp
    case "euro":
      return 1.11*gbp
    case "yuan":
      return 8.92*gbp
    case "yen":
      return 138.44*gbp

# -------------------------
# Main program
# -------------------------
gbp = float(input("Enter the number of Great British Pounds: "))
currency = input("Enter the currency (USD, Euro, Yuan, Yen): ").lower()
money = exchange(gbp, currency)
print(gbp, "GBP =", money, currency)

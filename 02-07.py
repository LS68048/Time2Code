# Nitrate program

# -------------------------
# Subprograms
# -------------------------
def calculate_dose(nitrate):
  if nitrate > 10:
    return 3
  elif nitrate > 2.5:
    return 2
  elif nitrate > 1:
    return 1
  else:
    return 0.5


# -------------------------
# Main program
# -------------------------
nitrate = float(input("Enter the nitrate level from the test: "))
carbon_dose = calculate_dose(nitrate)
print("For", nitrate, "nitrate dose", carbon_dose, "ml of carbon.")

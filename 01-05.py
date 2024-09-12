# Temperature converter program

# -------------------------
# Subprograms
# -------------------------
def c_to_f(centigrade):
  fahrenheit = centigrade * 1.8 + 32
  return fahrenheit

# -------------------------
# Main program
# -------------------------
centigrade = int(input("Enter the temperature in Centigrade: "))
fahrenheit = c_to_f(centigrade)
print(centigrade, "degrees Centigrade is", fahrenheit, "degrees Fahrenheit.")

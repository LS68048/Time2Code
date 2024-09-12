# States of water program

# -------------------------
# Subprograms
# -------------------------
def water_state(centigrade):
    if centigrade <= 0:
      return "solid"
    elif centigrade > 0 and centigrade < 100:
      return "liquid"
    else:
      return "gaseous"


# -------------------------
# Main program
# -------------------------

temperature = float(input("Enter the temperature in °C"))
state = water_state(temperature)
print("The water is in a", state, "state.")

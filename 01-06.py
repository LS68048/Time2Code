# Fish tank volume problem

# -------------------------
# Subprograms
# -------------------------

# Calculate the volume in cm3
def volume(length, width, height):
  return (length * width * height) / 1000

# Converts metric litres into imperial gallons
def litres_to_gallons(litres):
  return litres / 4.546


# -------------------------
# Main program
# -------------------------
length = int(input("Enter the length of the tank in cm: "))
width = int(input("Enter the width of the tank in cm: "))
height = int(input("Enter the height of the tank in cm: "))
litres = volume(length,width,height)
gallons = litres_to_gallons(litres)
print("A", length, "x", width, "x", height, "cm tank is", litres, "litres and", gallons, "imperial gallons.")

# Circle properties program

# -------------------------
# Subprograms
# -------------------------

# Calculate circle area from diameter
def circle_area(diameter):
  radius = diameter / 2
  return 3.14 * (radius * radius)

# Calculate circle circumference from diameter
def circle_circumference(diameter):
  return 3.14 * diameter
  

# -------------------------
# Main program
# -------------------------
diameter = float(input("Enter the diameter of the circle: "))
print(f"Area: {circle_area(diameter)}")
print(f"Circumference: {circle_circumference(diameter)}")

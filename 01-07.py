# Microscopy program

# -------------------------
# Subprograms
# -------------------------
def magnification(actual_size, image_size):
  return (image_size * 10000) / actual_size

# -------------------------
# Main program
# -------------------------
actual_size = int(input("Enter the actual size in micrometers: "))
image_size = int(input("Enter the image size in centimeters: "))
mag = magnification(actual_size, image_size)
print("The magnification is", mag ,"X")

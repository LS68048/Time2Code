# Periodic table program

# -------------------------
# Subprograms
# -------------------------

elems =[
  ["Li", "Lithium", 6.94, "Alkali Metals"],
  ["Na", "Sodium", 22.99, "Alkali Metals"],
  ["K", "Potassium", 39.098, "Alkali Metals"],
  ["F", "Flourine", 18.998, "Halogens"],
  ["Cl", "Chlorine", 35.45, "Halogens"],
  ["Br", "Bromine", 79.904, "Halogens"],
  ]

def periodic_table(elem):
  match elem:
    case "Li" | "Lithium":
      print(elems[0][0])
      print(elems[0][1])
      print(elems[0][2])
      print(elems[0][3])
    case "Na" | "Sodium":
      print(elems[1][0])
      print(elems[1][1])
      print(elems[1][2])
      print(elems[1][3])
    case "K" | "Potassium":
      print(elems[2][0])
      print(elems[2][1])
      print(elems[2][2])
      print(elems[2][3])
    case "F" | "Flourine":
      print(elems[3][0])
      print(elems[3][1])
      print(elems[3][2])
      print(elems[3][3])
    case "Cl" | "Chlorine":
      print(elems[4][0])
      print(elems[4][1])
      print(elems[4][2])
      print(elems[4][3])
    case "Br" | "Bromine":
      print(elems[5][0])
      print(elems[5][1])
      print(elems[5][2])
      print(elems[5][3])
    case _:
      print("Element is not in the catalogue")

# -------------------------
# Main program
# -------------------------

elem = input("Enter the symbol or name of an element: ")
periodic_table(elem)

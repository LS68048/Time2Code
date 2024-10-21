# Cookies program

# -------------------------
# Subprograms
# -------------------------
def read_cookie():
    prefs = open("preferences.txt", "r")
    theme = prefs.readline()
    return theme

def write_cookie(theme):
    prefs = open("preferences.txt", "w")
    prefs.write(theme)
    prefs.close()

def change_theme(theme):
    theme = "theme = dark" if theme == "theme = light" else "theme = light"
    write_cookie(theme)

# -------------------------
# Main program
# -------------------------
theme = read_cookie()
print("The current", theme)
swap = input("Do you want to swap the theme? (y/n): ")
if swap.lower() == "y":
    change_theme(theme)

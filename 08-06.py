# Morse code program

# -------------------------
# Subprograms
# -------------------------
def translate(morse):
    match morse:
        case ".-":
            return "A"
        case "-...":
            return "B"
        case "-.-.":
            return "C"
        case "-..":
            return "D"
        case ".":
            return "E"
        case "..-.":
            return "F"
        case "--.":
            return "G"
        case "....":
            return "H"
        case "..":
            return "I"
        case ".---":
            return "J"
        case "-.-":
            return "K"
        case ".-..":
            return "L"
        case "--":
            return "M"
        case "-.":
            return "N"
        case "---":
            return "O"
        case ".--.":
            return "P"
        case "--.-":
            return "Q"
        case ".-.":
            return "R"
        case "...":
            return "S"
        case "-":
            return "T"
        case "..-":
            return "U"
        case "...-":
            return "V"
        case ".--":
            return "W"
        case "-..-":
            return "X"
        case "-.--":
            return "Y"
        case "--..":
            return "Z"
        case _:
            return " "


def read_morse(filename):
    try:
        file = open(filename, "r")
        message = ""
        for line in file.readlines():
            for character in line.split(" "):
                message += translate(character)
        return message
    except FileNotFoundError:
        print("Error 404: File not found")

# -------------------------
# Main program
# -------------------------
filename = input("Enter the name of the file: ")
message = read_morse(filename)
print(message)

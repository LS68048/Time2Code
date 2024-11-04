# ini file program

# -------------------------
# Subprograms
# -------------------------
def input_settings():
    try:
        file = open("settings.ini", "r")
        name = ""
        server = ""
        port = ""
        for line in file.readlines():
            bits = line.split("=")
            if len(bits) == 1:
                continue
            if bits[0] == "name":
                name = bits[1]
            elif bits[0] == "server":
                server = bits[1]
            elif bits[0] == "port":
                port = bits[0]
        print("Last modified by:",name,"IP address:",server,"Port number:",port)
    except FileNotFoundError:
        print("settings.ini file not found.")

# -------------------------
# Main program
# -------------------------
input_settings()

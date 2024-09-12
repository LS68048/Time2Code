# Adder program

# -------------------------
# Subprograms
# -------------------------
def adder():
    total = 0
    top = 0
    bottom = 9999999999
    count = 0
    ave = 0
    complete = False
    while not complete:
        number = input("Enter number: ")
        if number != "e":
            number = float(number)
            total = total + number
            count = count + 1
            if number > top:
                top = number
            if number < bottom:
                bottom = number
        else:
            complete = True
            if count > 0:
                ave = total / count
            else:
                ave = 0
    print("Total:", total, "Top:", top, "Bottom:", bottom, "Ave:", ave)


# -------------------------
# Main program
# -------------------------
adder()

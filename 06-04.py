# Times tables program

# -------------------------
# Subprograms
# -------------------------
# Procedure to output the X times table.
def times_table(x):
    for i in range(1,13):
        print(i,"x",x,"=",i*x)

# -------------------------
# Main program
# -------------------------

table = int(input("Which table do you want to output? 1-12: "))
times_table(table)

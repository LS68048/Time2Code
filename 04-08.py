# Least common multiple program

# -------------------------
# Subprograms
# -------------------------
def lcm(number1, number2):
    if number1 > number2:
        count = number1
        while count % number1 != 0 or count % number2 != 0:
            count += 1
        return count
    else:
        count = number2
        while count % number1 != 0 or count % number2 != 0:
            count += 1
        return count

# -------------------------
# Main program
# -------------------------

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print(f"The LCM of {number1} and {number2} is {lcm(number1,number2)}")

# Fizz buzz program

# -------------------------
# Subprograms
# -------------------------
def fizz_buzz(x):
    num = 1
    while num <= x:
        if num % 3 == 0 and num % 5 == 0:
            print("Fizz Buzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        num += 1

# -------------------------
# Main program
# -------------------------

max = int(input("What number should the count be up to?: "))
fizz_buzz(max)
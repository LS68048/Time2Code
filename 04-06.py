# Guess the number program

# -------------------------
# Import libraries
# -------------------------
import random

# -------------------------
# Subprograms
# -------------------------
def play_guess_the_number(min, max):
    num = random.randint(min,max)
    guess = int(input("Enter the number I'm thinking of: "))
    attempts = 1
    
    while guess != num:
        if guess < num:
            print("Your guess is too low")
        elif guess > num:
            print("Your guess is too high")
        attempts += 1
        guess = int(input("Enter the number I'm thinking of: "))

    print(f"You've got it, I chose {num}. It took you {attempts} guesses")

# -------------------------
# Main program
# -------------------------
min = int(input("What is the lowest number I can choose? "))
max = int(input("What is the highest number I can choose? "))

print("OK, let's play. How many guesses will you take?")
play_guess_the_number(min,max)
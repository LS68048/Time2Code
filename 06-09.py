# Distribution of two dice program

# -------------------------
# Import libraries
# -------------------------
import random

# -------------------------
# Subprograms
# -------------------------
def distribution(num):
    tally = [0,0,0,0,0,0,0,0,0,0,0]
    count = 0
    while count < num:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        tally[dice1+dice2-2] += 1
        count += 1
    for i in range(10):
        print(str(i+2)+":",tally[i])
# -------------------------
# Main program
# -------------------------
num = int(input("How many times do you want to roll two dice?"))
distribution(num)

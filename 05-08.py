# Cut the deck program

# -------------------------
# Import libraries
# -------------------------
import random

# -------------------------
# Subprograms
# -------------------------

def play_game():
    random.shuffle(deck)
    card = deck[int(input("What number card do you want to draw? 0-34: "))]
    print("You reveal the",card)
    deck.pop(deck.index(card))
    cpu = deck[random.randint(0,34)]
    print("The CPU reveals the",cpu)
    output_winner(card,cpu)

def output_winner(card, cpu):
    if card[0] not in ["K","J","Q","A"] and cpu[0] not in ["K","J","Q","A"]:
        if int(card[0]) > int(cpu[0]):
            print("You Win!")
        elif int(card[0]) < int(cpu[0]):
            print("CPU wins.")
        elif int(card[0]) == int(cpu[0]):
            if cards.index(card) > cards.index(cpu):
                print("You Win!")
            elif cards.index(card) < cards.index(cpu):
                print("CPU Wins.")
    else:
        value_card = 0
        value_cpu = 0
        if card[0] in ["K","J","Q","A"]:
            value_card = ["J","Q","K","A"].index(card[0]) + 11
        if cpu[0] in ["K","J","Q","A"]:
            value_cpu = ["J","Q","K","A"].index(cpu[0]) + 11
        if value_card == 0:
            value_card = int(card[0])
        if value_cpu == 0:
            value_cpu = int(cpu[0])
        if value_cpu > value_card:
            print("CPU Wins.")
        elif value_card > value_cpu:
            print("You Win!")
        elif value_card == value_cpu:
            if cards.index(card) > cards.index(cpu):
                print("You Win!")
            elif cards.index(card) < cards.index(cpu):
                print("CPU Wins.")

# -------------------------
# Main program
# -------------------------
random.seed(0)
# The value order of the cards for reference
cards = ["6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC",
         "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD",
         "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH",
         "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS"]
deck = cards
play_game()

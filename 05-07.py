# Darts program

# -------------------------
# Subprograms
# -------------------------
def is_dart_valid(dart):
    if dart > 0 and dart < 20:
        return True
    elif dart == 25 or dart == 50:
        print("Shot!")
        return True
    elif dart <= 40 and dart % 2 == 0:
        print("Double",dart//2)
        return True
    elif dart <= 60 and dart % 3 == 0:
        print("Treble",dart//3)
        return True
    else:
        return False

def play_game():
    win = False
    turn = 0
    while not win:
        print("Player",turn+1,"it's your turn. Your score is:",score[turn])
        darts = 0
        scored = 0
        while darts < 3:
            print("Dart",darts+1)
            dart = int(input("Enter score: "))
            if is_dart_valid(dart):
                darts += 1
                score[turn] -= dart
                scored += dart
            if score[turn] <= 0:
                print("Player",turn+1,"wins the leg.")
                darts = 3
                win = True
        print(scored,"scored.")
        turn = not turn
    


# -------------------------
# Main program
# -------------------------

score = [501,501]
play_game()

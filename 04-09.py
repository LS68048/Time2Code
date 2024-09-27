# Rock, paper, scisssors program

# -------------------------
# Import libraries
# -------------------------
import random

# -------------------------
# Subprograms
# -------------------------
def get_player_choice():
    choice = input("Enter rock, paper, scissors (r/p/s): ")
    while not choice in ["r","p","s"]:
        choice = input("Enter rock, paper, scissors (r/p/s): ")
    return choice

def convert(rps):
    match rps:
        case "r":
            return "rock"
        case "p":
            return "paper"
        case "s":
            return "scissors"

def cpu_choice():
    return ["r","p","s"][random.randint(0,2)]

def who_won_round(player,cpu):
    if player == cpu:
        return "draw"
    else:
        rps_dict = {
            "r": ["s", "r", "p"],
            "p": ["r", "p", "s"],
            "s": ["p", "s", "r"],
        }
        choice_list = rps_dict[player]
        cpu_choice_index = choice_list.index(cpu)
        match cpu_choice_index:
            case 0:
                return "player"
            case 1:
                return "draw"
            case 2:
                return "cpu"

def play_game():
    cpu_score = 0
    player_score = 0

    while cpu_score < 5 and player_score < 5:
        print("player score:",player_score)
        print("cpu score:",cpu_score)

        player_choice = get_player_choice()
        npc_choice = cpu_choice()

        winner = who_won_round(player_choice, npc_choice)
        player_choice = convert(player_choice)
        npc_choice = convert(npc_choice)
        if winner == "player":
            print("player's",player_choice,"beat cpu's",npc_choice,"\n")
            player_score += 1
        elif winner == "cpu":
            print("cpu's",npc_choice,"beat player's",player_choice,"\n")
            cpu_score += 1
        else:
            print(player_choice,"-",npc_choice,"- it's a draw.\n")
    
    if player_score == 5:
        print("PLAYER WINS!")
    else:
        print("CPU WINS!")


# -------------------------
# Main program
# -------------------------

play_game()
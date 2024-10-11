# London Underground program

# -------------------------
# Subprograms
# -------------------------
def get_station():
    station = input("Enter Station: ")
    while not station.lower() in stations:
        station = input("Invalid. Enter Station: ")
    return station

def calculate_stops(ticket):
    order1 = stations.index(ticket[0])
    order2 = stations.index(ticket[1])
    if order1 > order2:
        return order1-order2
    else:
        return order2-order1

# -------------------------
# Main program
# -------------------------
# Victoria line
stations = ["brixton", "stockwell", "vauxhall", "pimlico", "victoria", "green park", "oxford circus", "warren street", "euston", "king's cross", "highbury & islington", "finsbury park", "seven sisters", "tottenham hale", "blackhorse road", "walthamstow central"]

first_station = get_station()
second_station = get_station()

stops = calculate_stops([first_station, second_station])

if stops == 1:
    print(first_station,"to",second_station,"is 1 stop.")
else:
    print(first_station,"to",second_station,"is", stops,"stops.")
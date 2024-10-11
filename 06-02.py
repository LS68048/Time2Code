# Rainfall program

# -------------------------
# Subprograms
# -------------------------
def analyse1(data):
    count = 0
    total = 0
    avg = 0
    high = 0
    for value in data:
        if value == 0:
            count = count + 1
        total += 1
        if value > high:
            high = value
    avg = sum(data)/total
    return [count,avg,high]


def analyse2(data):
    count = 0
    total = 0
    avg = 0
    high = 0
    for index in range(len(data)):
        if data[index] == 0:
            count = count + 1
        total += 1
        if value > high:
            high = value
    avg = sum(data)/total
    return [count,avg,high]


# -------------------------
# Main program
# -------------------------
daily_rainfall_mm = [0.1, 0.0, 0.2, 0.4, 0.1, 0.0, 0.0,
                     0.0, 0.3, 0.3, 0.2, 0.0, 0.0, 0.1]

data = analyse1(daily_rainfall_mm)
print("Days with no rain:", data[0])
print("Average rainfall:", round(data[1],2))
print("Highest rainfall:", data[2])

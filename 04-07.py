# Seconds in a day program

# -------------------------
# Subprograms
# -------------------------
def seconds_to_hours(seconds):
    return seconds // 3600


def seconds_to_minutes(seconds):
    return seconds // 60 % 60


def seconds_remaining(seconds):
    return seconds % 60


# -------------------------
# Main program
# -------------------------
seconds = int(input("Enter the number of seconds: "))
minutes = seconds_to_minutes(seconds)
hours = seconds_to_hours(seconds)
seconds = seconds_remaining(seconds)
print(hours, "hours", minutes, "minutes", seconds, "seconds")

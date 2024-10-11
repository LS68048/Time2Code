# Twelve days of Christmas program

# -------------------------
# Subprograms
# -------------------------
def output_song():
    days = ["second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth"]
    presents = ["and a partridge in a pear tree", "two turtle doves", "three french hens", "four calling birds", "five golden rings", "six geese laying", "seven swans swimming", "eight maids milking", "nine ladies dancing", "ten lords leaping", "eleven pipers piping", "twelve drummers drumming"]
    print("on the first day of Christmas\nMy true love gave to me\nA partridge in a pear tree\n")
    for i in range(11):
        print("on the",days[i],"day of Christmas\nMy true love gave to me")
        for j in range(i+1,-1,-1):
            print(presents[j])
        print("")

# -------------------------
# Main program
# -------------------------
output_song()
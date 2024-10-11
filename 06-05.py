# Voting count program

# -------------------------
# Subprograms
# -------------------------
def count_votes(ballot):
    a= 0
    b = 0
    c = 0
    d = 0
    for vote in ballot:
        if vote == "A":
            a += 1
            continue
        elif vote == "B":
            b += 1
            continue
        elif vote == "C":
            c += 1
        elif vote == "D":
            d += 1
    return [a,b,c,d]
                
# -------------------------
# Main program
# -------------------------
votes = ["A", "B", "B", "B", "B", "C", "C", "D", "A", "B",
         "A", "B", "A", "B", "D", "B", "C", "B", "B", "A"]

result = count_votes(votes)

print("Answer A:", result[0])
print("Answer B:", result[1])
print("Answer C:", result[2])
print("Answer D:", result[3])

# Tweet program

# -------------------------
# Subprograms
# -------------------------
def tweets(message, num_chars):
    messages = []
    if len(message) > num_chars:
        for i in range(0,len(message)//num_chars+1):
            messages.append(message[i*num_chars:i*num_chars+num_chars])
    else:
        messages.append(message)
    return messages


# -------------------------
# Main program
# -------------------------
message = input("Enter the message: ")
max_chars = int(input("How many characters per message? :"))
print(tweets(message, max_chars))

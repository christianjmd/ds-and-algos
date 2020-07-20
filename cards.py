"""
suits function:
 - function that sorts a given hand into four suits.
 -  alphabetical ranking.
 - output is nested list containing list of cards
"""
def suits(hand):

    output = [[], [], [], []]

    for j in range(1, len(hand), 2):
        if hand[j] == "C":                      # CLUBS
            output[0].append(hand[j-1])
            output[0].append(hand[j])
        if hand[j] == "D":                      # DIAMONDS
            output[1].append(hand[j-1])
            output[1].append(hand[j])
        if hand[j] == "H":                      # HEARTS
            output[2].append(hand[j-1])
            output[2].append(hand[j])
        if hand[j] == "S":                      # SPADES
            output[3].append(hand[j-1])
            output[3].append(hand[j])

    return output

"""
flush function:
 - determines whether a given hand is a flush.
"""

def flush(hand):

    check = []

    for i in range(len(hand)):  # loop takes the suit only hence hand[i][1]
        check.append(hand[i][1])

    if check[0::] == check[::-1]: # does symmetric check
        return True
    else:
        return False

"""
straight function:
 - function that determines whether a given hand is a straight.
"""

def straight(hand):
    check = []
    counter = 0

    for i in range(len(hand)):
        check.append(hand)
        check.sort()

    for j in range(len(check) - 1):
        if check[j] - check[j - 1] == -1:
            counter = counter + 1

    if counter == len(hand) - 1:
        return True
    else:
        return False

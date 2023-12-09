filepath = "input.txt"

def sort(aList, comp):
    for i in range(0,len(aList)):
        for j in range(i+1, len(aList)):
            if comp(aList[i], aList[j]):
                aList[i], aList[j] = aList[j], aList[i]

def typeOfHand(h):
    counts = [0,0,0,0,0] # one of a kind, two, three, four, five
    countedChars = []

    for char in h:
        if (char in countedChars):
            continue
        
        count = 0

        for ochar in h:
            if (char == ochar):
                count += 1

        counts[count - 1] += 1
        countedChars.append(char)

    if (counts[4] == 1): # five of a kind 
        return 7
    elif (counts[3] == 1): # four of a kind
        return 6
    elif ((counts[2] == 1) and (counts[1] == 1)): # full house (three and a pair)
        return 5
    elif (counts[2] == 1): # three of a kind
        return 4
    elif (counts[1] == 2): # two pairs
        return 3
    elif (counts[1] == 1): # one pair
        return 2
    else: # nothing 
        return 1
    
def jokerTypeOfHand(h):
    counts = [0,0,0,0,0] # one of a kind, two, three, four, five
    countedChars = []

    for char in h:
        if (char in countedChars):
            continue
        
        count = 0

        for ochar in h:
            if (char == ochar):
                count += 1

        counts[count - 1] += 1
        countedChars.append(char)

    if (counts[4] == 1): # five of a kind 
        return 7
    elif (counts[3] == 1): # four of a kind
        return 6
    elif ((counts[2] == 1) and (counts[1] == 1)): # full house (three and a pair)
        return 5
    elif (counts[2] == 1): # three of a kind
        return 4
    elif (counts[1] == 2): # two pairs
        return 3
    elif (counts[1] == 1): # one pair
        return 2
    else: # nothing 
        return 1

cardStrengths = {
    "A":13,
    "K":12,
    "Q":11,
    "J":10,
    "T":9,
    "9":8,
    "8":7,
    "7":6,
    "6":5,
    "5":4,
    "4":3,
    "3":2,
    "2":1
}

jokerCardStrengths = {
    "A":13,
    "K":12,
    "Q":11,
    "T":10,
    "9":9,
    "8":8,
    "7":7,
    "6":6,
    "5":5,
    "4":4,
    "3":3,
    "2":2,
    "J":1
}

def compareCards(c1, c2):
    return cardStrengths[c1] > cardStrengths[c2]

def jokerCompareCards(c1, c2):
    return jokerCardStrengths[c1] > jokerCardStrengths[c2]

def compareHands(h1, h2):
    t1 = typeOfHand(h1)
    t2 = typeOfHand(h2)

    if (t1 > t2):
        return True
    elif (t1 < t2):
        return False
    else:
        for i in range(5):
            if compareCards(h1[i], h2[i]):
                return True
            elif compareCards(h2[i], h1[i]):
                return False 
    
    return False

def jokerCompareHands(h1, h2):
    t1 = typeOfHand(h1)
    t2 = typeOfHand(h2)

    if (t1 > t2):
        return True
    elif (t1 < t2):
        return False
    else:
        for i in range(5):
            if jokerCompareCards(h1[i], h2[i]):
                return True
            elif jokerCompareCards(h2[i], h1[i]):
                return False 
            
def compare(h1,h2):
    return compareHands(h1[0], h2[0])

def jokerCompare(h1,h2):
    return jokerCompareHands(h1[0], h2[0])

handsAndBids = []

for line in open(filepath):
    hand = line[:5]
    bid = int(line[6:])
    handsAndBids.append((hand, bid))

sort(handsAndBids, compare)

rank = 1
totalwinnings = 0

for handAndBid in handsAndBids:
    totalwinnings += (rank * handAndBid[1])
    rank += 1

print("part 1:", totalwinnings)

sort(handsAndBids, jokerCompare)

rank = 1
totalwinnings = 0

for handAndBid in handsAndBids:
    totalwinnings += (rank * handAndBid[1])
    rank += 1

print("part 2:", totalwinnings)
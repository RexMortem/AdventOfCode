import re

filepath = "input.txt"

mappingTable = {}
mappings = {}

readFirst = False

currentCat = None
currentLine = 0

seeds = None

for line in open(filepath):
    if not readFirst:
        readFirst = True
        seeds = list(map(int, re.findall("[0-9]+",line)))
        continue

    mapLocation = line.find(" map")

    if not (mapLocation == -1): # initialise a mapping 
        firstDash = line.find("-")
        secondDash = line.find("-",firstDash+1)

        firstCat = line[:firstDash]
        secondCat = line[secondDash+1:mapLocation]

        mappings[firstCat] = secondCat 
        mappingTable[firstCat] = []
        currentCat = firstCat
    else:
        haveNumbers = re.search("[0-9]+", line)

        if not haveNumbers:
            continue 
        
        mappingTable[currentCat].append(list(map(int, re.findall("[0-9]+",line))))


def translateUsingMappings(mappingTable, value):
    for mapping in mappingTable:
        if (mapping[1] <= value < (mapping[1] + mapping[2])): # within range
            return (value - mapping[1]) + mapping[0]
        
    return value 

currentList = seeds
currentCat = "seed"

while (currentCat in mappings):
    nextList = []

    for dataPoint in currentList:
        nextList.append(translateUsingMappings(mappingTable[currentCat], dataPoint))
    
    currentList = nextList
    currentCat = mappings[currentCat]

print("minimum of few seeds (Part 1):",min(currentList))

currentList = []

for line in open(filepath):
    pairs = list(map(int, re.findall("[0-9]+", line)))

    first = True
    firstVal = None

    for value in pairs:
        if first:
            firstVal = value 
        else:
            for i in range(first,first + value):
                currentList.append(i) # way too slow; going through millions of values
        
        first = not first
    break

currentCat = "seed"

while (currentCat in mappings):
    nextList = []

    for dataPoint in currentList:
        nextList.append(translateUsingMappings(mappingTable[currentCat], dataPoint))
    
    currentList = nextList
    currentCat = mappings[currentCat]
    print(currentCat)

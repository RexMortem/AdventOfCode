import re

schematic = []

linen = 0
lastchar = 0

filepath = "input.txt"

for line in open(filepath):
    schematic.append([])
    charn = 0

    for char in line:
        schematic[linen].append(char)
        charn += 1

    lastchar = len(line) - 1
    linen += 1

# loading into 2D array used: could use regex to search top and bottom lines 

lastline = linen - 1
linen = 0

def checkChar(linen, i):
    char = schematic[linen][i]
    return not (char.isdigit() or (char == ".")) # not (char == ".") 

def searchNeighbours(linen, start, end): 
    for lineoffset in {-1,1}:
        lineToSearch = linen + lineoffset

        if not (0 <= lineToSearch <= lastline): # pythonic way to write conditionals 
            continue
        
        for i in range(max(start - 1,0), min(end + 1, lastchar+1)):
            if checkChar(lineToSearch, i):
                return True
            
    if (start > 0) and checkChar(linen, start - 1):
        return True
    
    if (end < lastchar) and checkChar(linen, end):
        return True
    
    return False

def replaceWithNum(linen, start, end, n):
    for i in range(start, end):
        schematic[linen][i] = f"{str(linen)}p:{str(start)}p;{str(n)}" # needs to be unique 

sum = 0

for line in open(filepath):
    indexoffset = 0 

    while True:
        numberMatch = re.search("[0-9]+", line)

        if not numberMatch:
            break
        
        si, ei = numberMatch.span()
        number = int(numberMatch.group())

        if searchNeighbours(linen, indexoffset + si, indexoffset + ei):
            sum += number

        replaceWithNum(linen, indexoffset + si, indexoffset + ei, number)

        line = line[ei:]
        indexoffset += ei

    linen += 1

def findAdjacentPartsToGear(linen, i):
    foundParts = []
    toReturn = []

    for xoffset in {-1,0,1}:
        for yoffset in {-1, 0, 1}:
            if (xoffset == 0 == yoffset):
                continue 
        
            x = i + xoffset 

            if not (0 <= x <= lastchar):
                continue

            y = linen + yoffset

            if not (0 <= y <= lastline):
                continue 

            potentialPart = schematic[y][x] 
            if len(potentialPart) == 1:
                continue 

            sindex = potentialPart.find("p;")
            if not sindex:
                continue 

            idpart = potentialPart[:sindex]
            if (idpart in foundParts):
                continue 
            
            print(potentialPart)

            foundParts.append(idpart)

            nindex = sindex + 2
            toReturn.append(int(potentialPart[nindex:]))

    return toReturn

gearsum = 0

linen = 0

for line in schematic:
    charn = 0

    for char in line:
        if char == "*":
            print(linen, charn)
            parts = findAdjacentPartsToGear(linen, charn)
    
            if len(parts) == 2: # is gear
                gearratio = 1

                for part in parts:
                    print("part: ",linen,charn,part)
                    gearratio *= part

                gearsum += gearratio

        charn += 1

    linen += 1

print("sum (part 1):", sum)
print("gearsum (part 2):", gearsum)
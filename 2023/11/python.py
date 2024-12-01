import re 

spaceMap = []
galaxies = []
emptyRows = [] 
filepath = "input.txt"

lineno = 0

for line in open(filepath):
    spaceMap.append(line.strip())
    if not re.search("#",line):
        emptyRows.append(lineno)
    else:
        start = 0
        while True:
            match = line.find("#",start)

            if match == -1:
                break
            else:
                galaxies.append((lineno, match))

            start = match + 1
    
    lineno += 1

emptyColumns = [] 

for x in range(len(spaceMap[0])):
    noGalaxies = True

    for y in range(lineno):
        if spaceMap[y][x] == "#":
            noGalaxies = False
            break 
    
    if noGalaxies:
        emptyColumns.append(x) 

def distanceBetweenGalaxies(g1, g2, expansionFactor):
    rawDifference = (abs(g2[0] - g1[0]), abs(g2[1] - g1[1]))
    xExpansion = 0
    yExpansion = 0

    xStep = (1 and (g2[1] > g1[1])) or -1
    yStep = (1 and (g2[0] > g1[0])) or -1
     
    for x in range(g1[1], g2[1], xStep):
        if x in emptyColumns: 
            xExpansion += expansionFactor
    
    for y in range(g1[0], g2[0], yStep):
        if y in emptyRows: 
            yExpansion += expansionFactor
    
    return rawDifference[0] + rawDifference[1] + xExpansion + yExpansion

steps = 0
part2steps = 0

for gi1 in range(len(galaxies)):
    for gi2 in range(gi1+1, len(galaxies)):
        steps += distanceBetweenGalaxies(galaxies[gi1], galaxies[gi2],1)
        part2steps += distanceBetweenGalaxies(galaxies[gi1], galaxies[gi2], 1000000 - 1)

print("Part 1: ", steps)
print("Part 2: ", part2steps)
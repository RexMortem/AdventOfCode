filepath = "input.txt"
pipes = []

sCoords = None

for line in open(filepath):
    pipes.append(line)
    index = line.find("S")
    
    if not (index == -1):
        sCoords = (len(pipes)-1, index)

maxY = len(pipes) - 1
maxX = len(pipes[0]) - 1

pipeTypes = {
    "S":{(0,1),(1,0),(0,-1),(-1,0)}, # first argument in pair is y (NORTH or SOUTH)
    "J":{(0, -1),(-1, 0)}, # north is negative, west is negative
    "L":{(0, 1),(-1, 0)},
    "7":{(0, -1),(1, 0)},
    "F":{(0, 1), (1, 0)},
    "-":{(0, 1), (0, -1)},
    "|":{(1, 0), (-1, 0)},
    ".":{}
}

# pipe is connected to another if they both feed into the other (via pipeTypes)
# we know there is one giant loop that we need to find (no junctions or crossroads so must be one path)

inBounds = lambda y,x: (0 <= x <= maxX) and (0 <= y <= maxY)
negTuple = lambda x: (-x[0], -x[1])

def getPathsForSymbol(y, x):
    potentialPaths = pipeTypes[pipes[y][x]]
    paths = []

    for offset in potentialPaths:
        ox = x + offset[1]
        oy = y + offset[0]

        if not (inBounds(oy, ox)):
            continue

        for oOffset in pipeTypes[pipes[oy][ox]]:
            if negTuple(offset) == oOffset:
                paths.append((oy, ox))
                break
    
    return paths

sPaths = getPathsForSymbol(sCoords[0], sCoords[1])
maxsteps = 0

for potentialCycle in sPaths:
    steps = 1
    cN = potentialCycle # y, x
    bDir = (sCoords[0] - cN[0], sCoords[1] - cN[1]) # backwards dir

    while (cN != sCoords):
        for offset in pipeTypes[pipes[cN[0]][cN[1]]]:
            if bDir == offset:
                continue 
            
            bDir = negTuple(offset)
            cN = (cN[0] + offset[0], cN[1] + offset[1])
            break

        steps += 1
    
    maxsteps = max(maxsteps, steps)

print("part 1:", maxsteps/2)
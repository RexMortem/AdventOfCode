filepath = "input.txt"

i = 0
instructions = []
nodeMap = {}

cN = "AAA"
# CRT: Chinese Remainder Theorem

for line in open(filepath):
    if (i == 0):
        for char in line:
            if (char == "L") or (char == "R"):
                instructions.append(char)
    elif len(line) > 15:
        sN = line[:3]
        lN = line[7:10]
        rN = line[12:15]
        
        nodeMap[sN] = (lN, rN)

    i += 1

steps = 0
cii = 0
lenInstructions = len(instructions)

while not (cN == "ZZZ"):
    ci = instructions[cii]

    if ci == "L":
        cN = nodeMap[cN][0]
    else:
        cN = nodeMap[cN][1]

    cii = (cii + 1) % lenInstructions
    steps += 1

print(steps)
filepath = "input.txt"

horizontalPatterns = []
verticalPatterns = []

for line in open(filepath):
    horizontalPatterns.append(line.strip())

for x in range(len(horizontalPatterns[0])):
    line = ""

    for y in range(len(horizontalPatterns)):
        line.append(horizontalPatterns[y][x])

    verticalPatterns.append(line)

def checkReflection(list, i):
    for j in range(len(list)):
        if (j > i): # already checked previous reflection
            return True 
         
        diff = i - j 
        k = int(i + diff) 

        if not (list[k] == list[j]):
            return False
        
for i in range(len(horizontalPatterns)):
    line = horizontalPatterns[i]

    for j in range(i+1, len(horizontalPatterns[0])):
        oline = horizontalPatterns[j]

        if (line == oline):
            midpoint = (line + oline)/2

            if checkReflection(horizontalPatterns, midpoint):

import re
filepath = "input.txt"

def getDifferences(history):
    differences = []
    same = True

    for i in range(len(history)-1):
        diff = history[i+1] - history[i]
        differences.append(diff)

        if not (diff == differences[0]):
            same = False 
        
    if same: 
        return differences[0], differences[0]
    else:
        ld, rd = getDifferences(differences)
        return differences[0] - ld, differences[len(differences) - 1] + rd
    
rsum = 0
lsum = 0
for line in open(filepath):
    history = list(map(int, re.findall("[0-9\-]+", line)))
    ld, rd = getDifferences(history)

    nextr = history[len(history)-1] + rd
    nextl = history[0] - ld

    rsum += nextr
    lsum += nextl

print("part 1:", rsum)
print("part 2:", lsum)

# 1581679977
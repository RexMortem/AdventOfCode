import re

bag={
    "red":12,
    "green":13,
    "blue":14
}

def checkGame(line):
    indexColon = line.find(":")
    afterNum = line[indexColon+1:len(line)]
    
    fail = False

    minVals={
        "red":0,
        "green":0,
        "blue":0
    }

    for x in afterNum.split(";"):
        while (True):
            digitMatch = re.search("[0-9]+", x) # span/group

            if not digitMatch:
                break

            digit = int(digitMatch.group())

            wordMatch = re.search("[a-z]+", x)
            
            _,end = wordMatch.span()

            if bag[wordMatch.group()] < digit:
                fail = True
                # break if only doing part 1 (validity)
            
            if minVals[wordMatch.group()] < digit:
                minVals[wordMatch.group()] = digit
            
            x = x[end:len(x)]

        #if fail: only use this if only doing part 1 (validity)
        #    break

    power = minVals["red"] * minVals["green"] * minVals["blue"]
    return not fail, power

sum = 0
sumPower = 0
i = 0

for line in open("input.txt"):
    i += 1
    isValid, power = checkGame(line)
    sumPower += power
    
    if isValid:
        sum += i
    
print(sum, sumPower)
import re

bag={
    "red":12,
    "green":13,
    "blue":14
}

print(re.search("([0-9]|\s)+","9 blue, 18 green, 4 red").group())

def checkValidGame(line):
    indexColon = line.find(":")
    afterNum = line[indexColon+1:len(line)]
    
    for x in afterNum.split(";"):
        print(x)
        #while ():
         #   match = re.search("([0-9]|\s)+", x) # span/group
           # _,end = match.span()
            #x = x[end:len(x)]
    return 0

sum = 0

for line in open("input.txt"):
    sum += checkValidGame(line)
    
print(sum)
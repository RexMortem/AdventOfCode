import sys

lines = sys.stdin.read().strip().split("\n")
lines 
l1 = []
l2 = []

print(lines)

for line in lines:
    l, r = map(int, line.split())
    l1.append(l)
    l2.append(r)

# Part 1

l1.sort()
l2.sort()

dist = 0

for i in range(len(l1)):
    dist += abs(l1[i] - l2[i])

print(dist)

# Part 2 

rHashMap = {}

for num in l2:
    rHashMap[num] = rHashMap.get(num, 0) + 1

similarity = 0

for num in l1:
    if num in rHashMap:
        similarity += num * rHashMap[num]
    
print(similarity)
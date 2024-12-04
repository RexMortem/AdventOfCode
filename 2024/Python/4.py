import itertools
import sys
import re
from collections import Counter

filePath = __file__.split("\\")
qNo = filePath[-1][:-3] 

pathToInput = __file__[:-1 * (len(filePath[-1])+len(filePath[-2]) + 1)] + "Input\\" + qNo + ".in" 

rows = None 

with open(pathToInput,"r") as file:
    rows = file.read().strip().split("\n")

# Part 1

word = "XMAS"

nRows = len(rows)
nColumns = len(rows[0])

def isOnBoard(y,x):
    return (0 <= y < nRows) and (0 <= x < nColumns)

def countXMASatX(y, x):
    localCount = 0

    for xOffset in (-1, 0, 1):
        for yOffset in (-1, 0, 1):
            if (xOffset == yOffset == 0):
                continue 
            
            matching = True 

            for i in range(1, len(word)):
                if not (isOnBoard(y + yOffset*i, x + xOffset*i) and (rows[y+yOffset*i][x+xOffset*i] == word[i])):
                    matching = False 
                    break
            
            if matching:
                localCount += 1 
    
    return localCount 

count = 0

for y in range(len(rows)):
    row = rows[y]

    for x in range(len(row)):
        if row[x] == 'X': # look in all directions now
            count += countXMASatX(y,x)

print(count)

# Part 2

def countMAS(y, x):
    if not (isOnBoard(y-1, x) and isOnBoard(y+1, x) and isOnBoard(y, x-1) and isOnBoard(y, x+1)): # we know y, x coords are on board if this statement is avoided
        return 0
    
    firstDiag = ((rows[y-1][x-1] == 'M') and (rows[y+1][x+1] == 'S')) or ((rows[y-1][x-1] == 'S') and (rows[y+1][x+1] == 'M'))
    secondDiag = ((rows[y-1][x+1] == 'M') and (rows[y+1][x-1] == 'S')) or ((rows[y-1][x+1] == 'S') and (rows[y+1][x-1] == 'M'))

    if firstDiag and secondDiag:
        return 1
    else:
        return 0
    

sCount = 0

for y in range(len(rows)):
    row = rows[y]

    for x in range(len(row)):
        if row[x] == 'A': # look in all directions now
            sCount += countMAS(y,x)

print(sCount)
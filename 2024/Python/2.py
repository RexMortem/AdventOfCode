import itertools
import sys

filePath = __file__.split("\\")
qNo = filePath[-1][:-3] 

lines = None 

pathToInput = __file__[:-1 * (len(filePath[-1])+len(filePath[-2]) + 1)] + "Input\\" + qNo + ".in" 

with open(pathToInput,"r") as file:
    lines = file.read().strip().split("\n")

print(lines)
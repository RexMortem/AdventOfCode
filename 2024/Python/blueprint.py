import itertools
import sys

filePath = __file__.split("\\")
qNo = filePath[-1][:-3] # taking advantage of the fact you can index backwards in this cursed language

lines = None 

pathToInput = __file__[:-1 * (len(filePath[-1])+len(filePath[-2]) + 1)] + "Input\\" + qNo + ".in" # (the +1 is because of the '\' in Python\blueprint.py)

with open(pathToInput,"r") as file:
    lines = file.read().strip().split("\n")

print(lines)
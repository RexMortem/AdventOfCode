import itertools
import sys
import re
from collections import Counter

filePath = __file__.split("\\")
qNo = filePath[-1][:-3] 

pathToInput = __file__[:-1 * (len(filePath[-1])+len(filePath[-2]) + 1)] + "Input\\" + qNo + ".in" 

lines = None 

with open(pathToInput,"r") as file:
    lines = file.read().strip().split("\n")

print(lines)
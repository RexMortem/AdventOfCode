import itertools
import sys
import re
from collections import Counter

filePath = __file__.split("\\")
qNo = filePath[-1][:-3] 

pathToInput = __file__[:-1 * (len(filePath[-1])+len(filePath[-2]) + 1)] + "Input\\" + qNo + ".in" 

search = None 

with open(pathToInput,"r") as file:
    search = file.read().strip()

matches = re.findall(r'mul\((\d+),(\d+)\)', search) # if we didn't make \d+ a group, then we'd get whole strings in our match input instead of tuples

ourSum = 0

for match in matches:
    l,r = int(match[0]), int(match[1])
    ourSum += l*r

print(ourSum)

# replace characters from don't() to do() with gibberish

search = re.sub(r"don't\(\)(.*?)do\(\)","foo", search,flags=re.DOTALL) # named 'foo' so it doesn't accidentally create a new don't -> Learned about greedy/lazy regex!
search = re.sub(r"don't\(\)(.)*","",search, flags=re.DOTALL) # search for ending "don't"s

matches = re.findall(r'mul\((\d+),(\d+)\)', search) 
ourSum = 0

for match in matches:
    l,r = int(match[0]), int(match[1])
    ourSum += l*r

print(ourSum)
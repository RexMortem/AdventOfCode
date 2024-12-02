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

safeCount = 0

for report in lines: 
    values = map(int, report.split())
    prevValue = None 
    increasing = None 
    reportVal = True 

    for value in values:
        if not prevValue:
            prevValue = value 
            continue 
        
        if increasing is None:
            if value > prevValue:
                increasing = True 
            else:
                increasing = False 
        else:
            if (increasing and (value < prevValue)):
                reportVal = False 
                break
            elif ((not increasing) and (value > prevValue)):
                reportVal = False 
                break

        # check other safe cond

        if reportVal and not (1 <= abs(value - prevValue) <= 3):
            reportVal = False 
        
        if not reportVal:
            break
    
        prevValue = value 
    
    if reportVal:
        safeCount += 1 
        
print(safeCount)

# Part 2 

def stdCheckReport(values):
    prevValue = None 
    increasing = None 
    reportVal = True 

    for value in values:
        if not prevValue:
            prevValue = value 
            continue 
        
        if increasing is None:
            if value > prevValue:
                increasing = True 
            else:
                increasing = False 
        else:
            if (increasing and (value < prevValue)):
                reportVal = False 
                break
            elif ((not increasing) and (value > prevValue)):
                reportVal = False 
                break

        # check other safe cond

        if reportVal and not (1 <= abs(value - prevValue) <= 3):
            reportVal = False 
        
        if not reportVal:
            break
    
        prevValue = value 
    
    return reportVal 

oSafeCount = 0

for report in lines: 
    values = list(map(int, report.split()))
    prevValue = None 
    increasing = None 
    reportVal = True 

    for i in range(len(values)):
        value = values[i]

        if not prevValue:
            prevValue = value 
            continue 
        
        if increasing is None:
            if value > prevValue:
                increasing = True 
            else:
                increasing = False 
        else:
            if (increasing and (value < prevValue)):
                reportVal = False 
            elif ((not increasing) and (value > prevValue)):
                reportVal = False 

        # check other safe cond

        if reportVal and not (1 <= abs(value - prevValue) <= 3):
            reportVal = False 
        
        
        if not reportVal:
            # let's see if we can save the report! Either remove value or prevValue or even prevPrevValue
            A = values.copy()
            A.pop(i)
            reportVal = stdCheckReport(A)

            if reportVal:
                break

            # let's try with removing prevValue instead...
            B = values.copy()
            B.pop(i-1)
            reportVal = stdCheckReport(B)

            if reportVal or (i <= 1):
                break

            # removing prevPrevValue
            C = values.copy()
            C.pop(i-2)
            reportVal = stdCheckReport(C)

            break

        prevValue = value 

    if reportVal:
        #print("safe:", report)
        oSafeCount += 1 
    else:
        #print("unsafe:", report)
        pass
        
print(oSafeCount)
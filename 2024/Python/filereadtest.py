import timeit

filePath = __file__.split("\\")
qNo = filePath[-1][:-3] # taking advantage of the fact you can index backwards in this cursed language

pathToInput = __file__[:-1 * (len(filePath[-1])+len(filePath[-2]) + 1)] + "Input\\" + qNo + ".in" # (the +1 is because of the '\' in Python\blueprint.py)

# Methods 

def method1():
    lines = None 

    with open(pathToInput,"r") as file:
        lines = file.read().strip().split("\n")

def method2():
    lines = open(pathToInput,"r").read().strip().split("\n")

def method3():
    lines = open(pathToInput,"r").readlines()

methods = [method1, method2, method3]

# Let's time them

for i in range(len(methods)):
    print(f"Method {i+1}: {timeit.timeit(stmt=methods[i], number=500)}")

# inconsistent BUT Method 1 is generally fastest
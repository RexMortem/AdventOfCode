import re

print(sum([int(re.search("[0-9]", line).group() + re.search("[0-9]",line[::-1]).group()[::-1]) for line in open("input.txt")]))
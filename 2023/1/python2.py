import re

pattern = "(one|two|three|four|five|six|seven|eight|nine|[0-9])"
reversepattern = "(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|[0-9])"

wordsToNum = {
    "zero":"0",
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}

def wordCase(x):
    if (not x.isdigit()):
        return wordsToNum[x]
    else:
        return x

print(sum([int(wordCase(re.search(pattern, line).group()) + wordCase(re.search(reversepattern,line[::-1]).group()[::-1])) for line in open("input.txt")]))
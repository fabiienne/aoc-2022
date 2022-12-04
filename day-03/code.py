from curses.ascii import isupper
from pathlib import Path

inputFile = Path(__file__).with_name('input.txt').open('r')
data= inputFile.read().splitlines()

def charToInt(char):
    return ord(char)-38 if isupper(char) else ord(char) -96

def part1(data):
    sum= 0
    for line in data:
        s1, s2 = line[:len(line)//2], line[len(line)//2:]
        char= list(set(s1).intersection(set(s2)))[0]
        sum += charToInt(char)
    return sum

def part2(data):
    sum = 0
    return sum

print(part1(data))
print(part2(data))
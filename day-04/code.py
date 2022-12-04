from curses.ascii import isupper
from hashlib import shake_128
from pathlib import Path

inputFile = Path(__file__).with_name('input.txt').open('r')
data= inputFile.read().splitlines()

def part1(lines):
    sum= 0
    for line in lines:
     s1,s2= line.split(',')
     a, b = list(map(int, s1.split('-')))
     c, d = list(map(int, s2.split('-')))
     if (a>=c and b<=d) or (c>=a and d<=b): 
        sum += 1
    return  sum

print(part1(data))
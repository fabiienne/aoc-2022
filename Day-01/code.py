#find the elve who is carrying the most amount of calories
from numpy import append


data= open('/Users/fabiennehaas/aoc-2022/day-01/input2.txt','r')
calories= data.read().strip().split("\n\n")

print(calories)
calories_int= [sum([int(c)for c in elf.splitlines()])for elf in calories]

print(calories_int)
a1= max(calories_int)
print(a1)
a2= sorted(calories_int)
print(a2)
last = sum(a2[-1:-4:-1])
print(last)

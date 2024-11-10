import itertools
from more_itertools import windowed

potions = {
        'x':0,
        'A':0,
        'B':1,
        'C':3,
        'D':5
        }

with open("input1.txt") as file:
    data1 = file.read().strip()
with open("input2.txt") as file:
    data2 = file.read().strip()
with open("input3.txt") as file:
    data3 = file.read().strip()

def part1(data):
    return sum(map(lambda c: potions[c],data))

def part2(data):
    total = 0
    for a,b in windowed(data,2,step=2):
        total += potions[a] + potions[b]
        if a!='x' and b!='x':
            total += 2
    return total

def partx(data,x:int):
    total = 0
    for wind in windowed(data,x,step=x):
        enemies = sum(c != 'x' for c in wind)
        if enemies == 2:
            total += 2
        if enemies == 3:
            total += 6
        for c in wind:
            total += potions[c]
    return total

assert part2("Ax")==0
assert part2("BC")==6
assert part2("CA")==5
    
print(part1(data1))
print(part2(data2))
print(partx(data3,3))

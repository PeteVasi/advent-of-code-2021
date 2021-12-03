#!/usr/bin/env python3

lines = []
with open("input.txt", 'r') as f:
    lines = f.readlines()

aim = 0
horiz = 0
depth = 0
for line in lines:
    (dir, amount) = line.split()
    if dir == "forward":
        horiz += int(amount)
        depth += aim * int(amount)
    elif dir == "down":
        aim += int(amount)
    elif dir == "up":
        aim -= int(amount)

print(f"Horiz: {horiz}, Depth: {depth} :: Product: {horiz*depth}")

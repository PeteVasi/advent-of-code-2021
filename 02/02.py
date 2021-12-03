#!/usr/bin/env python3

lines = []
with open("input.txt", 'r') as f:
    lines = f.readlines()

horiz = 0
depth = 0
for line in lines:
    (dir, amount) = line.split()
    if dir == "forward":
        horiz += int(amount)
    elif dir == "down":
        depth += int(amount)
    elif dir == "up":
        depth -= int(amount)

print(f"Horiz: {horiz}, Depth: {depth} :: Product: {horiz*depth}")

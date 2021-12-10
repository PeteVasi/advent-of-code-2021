#!/usr/bin/env python3

heightmap = []
with open("input.txt", 'r') as f:
    line = f.readline()
    while line:
        heightmap.append([int(n) for n in line.strip()])
        line = f.readline()

lowest = 0
risk = 0
for y in range(len(heightmap)):
    for x in range(len(heightmap[y])):
        if (y == 0 or heightmap[y][x] < heightmap[y-1][x]) and \
           (y == len(heightmap) - 1 or heightmap[y][x] < heightmap[y+1][x]) and \
           (x == 0 or heightmap[y][x] < heightmap[y][x-1]) and \
           (x == len(heightmap[y]) - 1 or heightmap[y][x] < heightmap[y][x+1]):
           lowest += 1
           risk += 1 + heightmap[y][x]

print(f"Lowest points: {lowest}, risk value: {risk}")

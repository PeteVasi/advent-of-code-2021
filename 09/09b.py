#!/usr/bin/env python3

def floodfill(hmap, x, y):
    if x < 0 or y < 0 or y >= len(hmap) or x >= len(hmap[y]) or hmap[y][x] >= 9:
        return 0
    else:
        hmap[y][x] = 99
        filled = 1
        filled += floodfill(hmap, x+1, y)
        filled += floodfill(hmap, x-1, y)
        filled += floodfill(hmap, x, y+1)
        filled += floodfill(hmap, x, y-1)
        return filled

heightmap = []
with open("input.txt", 'r') as f:
    line = f.readline()
    while line:
        heightmap.append([int(n) for n in line.strip()])
        line = f.readline()

basins = []
for y in range(len(heightmap)):
    for x in range(len(heightmap[y])):
        h = floodfill(heightmap, x, y)
        if h > 0:
            basins.append(h)
basins.sort(reverse=True)

print(f"Basins: {basins}, top 3: {basins[0]*basins[1]*basins[2]}")

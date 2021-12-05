#!/usr/bin/env python3

import re

def drawline(img, line):
    if line[2] > line[0]:
        (x1, y1, x2, y2) = line
    else:
        (x2, y2, x1, y1) = line
    dx = x2 - x1
    dy = y2 - y1
    if dx != 0:
        for x in range(x1, x2+1):
            y = int(y1 + dy * (x - x1) / dx)
            img[y][x] += 1
    elif y2 > y1:
        for y in range(y1, y2+1):
            img[y][x1] += 1
    else:
        for y in range(y2, y1+1):
            img[y][x1] += 1


lines = []
with open("input.txt", 'r') as f:
    line = f.readline()
    while line:
        lines.append([int(n) for n in re.findall("\d+", line)])
        line = f.readline()

img = []
for i in range(1000):
    img.append([0] * 1000)

for line in lines:
    if line[0] == line[2] or line[1] == line[3]:
        drawline(img, line)

#for line in img:
#    print(f"{line}")

score = 0
for line in img:
    for point in line:
        if point > 1:
            score += 1
print(f"Score: {score}")

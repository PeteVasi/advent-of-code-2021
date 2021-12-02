#!/usr/bin/env python3

import sys

lines = []
with open("input1.txt", 'r') as f:
    lines = f.readlines()

increases = 0
last = sys.maxsize
for i in range(2, len(lines)):
    cur = int(lines[i-2]) + int(lines[i-1]) + int(lines[i])
    if cur > last:
        increases += 1
    last = cur

print("Increased: " + str(increases))

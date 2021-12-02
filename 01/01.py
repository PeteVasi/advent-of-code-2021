#!/usr/bin/env python3

import sys

lines = []
with open("input1.txt", 'r') as f:
    lines = f.readlines()

increases = 0
last = sys.maxsize
for line in lines:
    i = int(line)
    if i > last and i > 0:
        increases += 1
    last = i

print("Increased: " + str(increases))

#!/usr/bin/env python3

import sys

with open("input.txt", 'r') as f:
    horiz = [int(n) for n in f.readline().strip().split(',')]

minfuel = sys.maxsize
for i in range(max(horiz)):
    fuel = 0
    for h in horiz:
        fuel += abs(h - i)
    if fuel < minfuel:
        minfuel = fuel

print(f"Minimum fuel: {minfuel}")

#!/usr/bin/env python3

patterns = []
digits = []
with open("input.txt", 'r') as f:
    line = f.readline()
    while line:
        (pattern, digit) = line.split('|')
        patterns.append([p.strip() for p in pattern.strip().split()])
        digits.append([d.strip() for d in digit.strip().split()])
        line = f.readline()

unique = 0
for digit in digits:
    for d in digit:
        if len(d) in [2, 3, 4, 7]:
            unique += 1

print(f"Uniques: {unique}")

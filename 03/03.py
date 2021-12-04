#!/usr/bin/env python3

lines = []
with open("input.txt", 'r') as f:
    lines = f.readlines()

ones = []
zeroes = []
for i in range(0, len(lines[0])-1):
    ones.append(0)
    zeroes.append(0)
for line in lines:
    for i, c in enumerate(line):
        if c == '1':
            ones[i] += 1
        elif c == '0':
            zeroes[i] += 1

print(f"ones: {ones}, zeroes: {zeroes}")

gamma = 0
epsilon = 0
for i in range(0, len(lines[0])-1):
    if ones[i] > zeroes[i]:
        gamma = (gamma * 2) + 1
        epsilon *= 2
    else:
        gamma *= 2
        epsilon = (epsilon * 2) + 1

print(f"Gamma: {gamma}, Epsilon {epsilon} :: Product {gamma*epsilon}")

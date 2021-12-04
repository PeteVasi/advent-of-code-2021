#!/usr/bin/env python3

lines = []
with open("input.txt", 'r') as f:
    lines = f.readlines()
nums = [int(line, 2) for line in lines]

bits = len(lines[0].strip())
ones = [0] * bits
zeroes = [0] * bits
for num in nums:
    for i in range(bits):
        if (num >> (bits - i - 1)) & 1 == 1:
            ones[i] += 1
        else:
            zeroes[i] += 1

gamma = 0
epsilon = 0
for i in range(bits):
    if ones[i] > zeroes[i]:
        gamma = (gamma << 1) + 1
        epsilon <<= 1
    else:
        gamma <<= 1
        epsilon = (epsilon << 1) + 1

print(f"Gamma: {gamma}, Epsilon {epsilon} :: Product {gamma*epsilon}")

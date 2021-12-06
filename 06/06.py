#!/usr/bin/env python3

with open("input.txt", 'r') as f:
    fishlife = [int(n) for n in f.readline().strip().split(',')]

fishes = [0] * 9
for fish in fishlife:
    fishes[fish] += 1

#for i in range(80):
for i in range(256):
    spawn = fishes.pop(0)
    fishes[6] += spawn
    fishes.append(spawn)

print(f"Total fishes: {sum(fishes)}")

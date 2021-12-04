#!/usr/bin/env python3

lines = []
with open("input.txt", 'r') as f:
    lines = f.readlines()
nums = [int(line, 2) for line in lines]

bits = len(lines[0].strip())
oxygen = nums.copy()
scrubber = nums.copy()
for i in range(bits):
    ones = 0
    zeroes = 0
    for o in oxygen:
        if (o >> (bits - i - 1)) & 1 == 1:
            ones += 1
        else:
            zeroes += 1
    oxygen = [o for o in oxygen if (ones >= zeroes and (o >> (bits - i - 1)) & 1 == 1) or (ones < zeroes and (o >> (bits - i - 1)) & 1 == 0)]
    if len(oxygen) == 1:
        oxygenval = oxygen[0]

    ones = 0
    zeroes = 0
    for s in scrubber:
        if (s >> (bits - i - 1)) & 1 == 1:
            ones += 1
        else:
            zeroes += 1
    scrubber = [s for s in scrubber if (ones < zeroes and (s >> (bits - i - 1)) & 1 == 1) or (ones >= zeroes and (s >> (bits - i - 1)) & 1 == 0)]
    if len(scrubber) == 1:
        scrubberval = scrubber[0]

print(f"Oxygen: {oxygenval}, Scrubber {scrubberval} :: Product {oxygenval*scrubberval}")

#!/usr/bin/env python3

"""
   1:      4:      7:      8:  
  ....    ....    aaaa    aaaa 
 .    c  b    c  .    c  b    c
 .    c  b    c  .    c  b    c
  ....    dddd    ....    dddd 
 .    f  .    f  .    f  e    f
 .    f  .    f  .    f  e    f
  ....    ....    ....    gggg 
   2       4        3      7   
   *       *        *      *   

   0:      6:      9:
  aaaa    aaaa    aaaa
 b    c  b    .  b    c
 b    c  b    .  b    c
  ....    dddd    dddd
 e    f  e    f  .    f
 e    f  e    f  .    f
  gggg    gggg    gggg
   6       6        6
 1 not 4  not 1     4

   2:      3:      5:  
  aaaa    aaaa    aaaa 
 .    c  .    c  b    .
 .    c  .    c  b    .
  dddd    dddd    dddd 
 e    .  .    f  .    f
 e    .  .    f  .    f
  gggg    gggg    gggg 
   5       5       5   
 2 of 4    1     3 of 4
"""


def getDigit(digit, pattern):
    if len(digit) == 2:
        return 1
    elif len(digit) == 4:
        return 4
    elif len(digit) == 3:
        return 7
    elif len(digit) == 7:
        return 8
    else:
        one = [set(p) for p in pattern if len(p) == 2][0]
        four = [set(p) for p in pattern if len(p) == 4][0]
        if len(digit) == 6:
            if four.issubset(set(digit)):
                return 9
            elif one.issubset(set(digit)):
                return 0
            else:
                return 6
        else: # len(digit) == 5
            if one.issubset(set(digit)):
                return 3
            elif len(four.difference(set(digit))) == 2:
                return 2
            else:
                return 5


patterns = []
digits = []
with open("input.txt", 'r') as f:
    line = f.readline()
    while line:
        (pattern, digit) = line.split('|')
        patterns.append([p.strip() for p in pattern.strip().split()])
        digits.append([d.strip() for d in digit.strip().split()])
        line = f.readline()

sum = 0
for i in range(len(digits)):
    digit = getDigit(digits[i][0], patterns[i]) * 1000 + getDigit(digits[i][1], patterns[i]) * 100 + getDigit(digits[i][2], patterns[i]) * 10 + getDigit(digits[i][3], patterns[i])
    sum += digit
    #print(f"Digit: {digit}")

print(f"Sum: {sum}")

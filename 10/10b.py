#!/usr/bin/env python3

from os import linesep


with open("input.txt", 'r') as f:
    lines = f.readlines()

scores = []
for line in lines:
    opens = []
    for char in line.strip():
        if char in ['(', '[', '{', '<']:
            opens.append(char)
        else:
            opened = opens.pop()
            if (char == ')' and opened != '(') or \
               (char == ']' and opened != '[') or \
               (char == '}' and opened != '{') or \
               (char == '>' and opened != '<'):
               opens = []
               break
    if len(opens) > 0:
        linescore = 0
        print(f"Incomplete: {opens}")
        for i in range(len(opens)):
            char = opens.pop()
            if char == '(':
                linescore = linescore * 5 + 1
            elif char == '[':
                linescore = linescore * 5 + 2
            elif char == '{':
                linescore = linescore * 5 + 3
            elif char == '<':
                linescore = linescore * 5 + 4
        print(f"Line score: {linescore}")
        scores.append(linescore)

scores.sort()
mid = int((len(scores) - 1) / 2)
print(f"Completion scores: {scores}")
print(f"Middle score: {scores[mid]}")

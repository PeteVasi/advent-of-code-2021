#!/usr/bin/env python3

with open("input.txt", 'r') as f:
    lines = f.readlines()

score = 0
for line in lines:
    opens = []
    for char in line.strip():
        if char in ['(', '[', '{', '<']:
            opens.append(char)
        elif len(opens) == 0:
            print(f"Closing {char} without open.")
            break
        else:
            opened = opens.pop()
            if (char == ')' and opened != '(') or \
               (char == ']' and opened != '[') or \
               (char == '}' and opened != '{') or \
               (char == '>' and opened != '<'):
               print(f"Closing {char} attempted to close an opening {opened}.")
               if char == ')':
                   score += 3
               elif char == ']':
                   score += 57
               elif char == '}':
                   score += 1197
               elif char == '>':
                   score += 25137
               break

print(f"Error score: {score}")

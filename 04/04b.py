#!/usr/bin/env python3

import sys

def isWin(nums, board):
    for i in range(5):
        if board[i*5] in nums and board[i*5+1] in nums and board[i*5+2] in nums and board[i*5+3] in nums and board[i*5+4] in nums:
            return True
        if board[i] in nums and board[i+5] in nums and board[i+10] in nums and board[i+15] in nums and board[i+20] in nums:
            return True
    return False


boards = []
with open("input.txt", 'r') as f:
    nums = [int(n) for n in f.readline().strip().split(',')]
    _ = f.readline()
    while _:
        board = []
        for i in range(5):
            board.extend([int(n) for n in f.readline().strip().split()])
        boards.append(board)
        _ = f.readline()

for i in range(5, len(nums)):
    if len(boards) == 1 and isWin(nums[:i], boards[0]):
        scoreboard = sum([n for n in boards[0] if n not in nums[:i]])
        print(f"Scoreboard: {scoreboard}, on num: {nums[i-1]} :: final score: {scoreboard*nums[i-1]}")
        sys.exit()
    boards = [board for board in boards if not isWin(nums[:i], board)]

# Loc - FunProgramming

# Rock, Paper, Scissor, by Ak Sweigart
# A program to play rock-paper-scissor

import random, time, sys

print('ROCK, PAPER, SCISSOR')

# Keep track of the numbers of wins, losses, and ties.
wins, losses, ties = 0, 0, 0

while True: # main loop
	while True: # keep asking until player enters R/P/S/Q
		print(f'{wins} Wins, {losses} Losses, {ties} Ties')
		print('Enter your move: (R)ock (P)aper (S)cissor or (Q)uit')
		playerMove = input().upper()
		if playerMove == 'Q':
			sys.exit() # exit out the system

		if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
			break
	
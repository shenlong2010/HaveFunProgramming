# Loc - FunProgramming

# Rock, Paper, Scissor, by Al Sweigart
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
		else:
			print('Type one of of R, P, S, or Q.')

	if playerMove == 'R':
		print('ROCK versus...')
		playerMove = 'ROCK'
	elif playerMove == 'P':
		print('PAPER versus...')
		playerMove = 'PAPER'
	elif playerMove == 'S':
		print('SCISSOR versus...')
		playerMove = 'SCISSOR'

	# print({'R': 'ROCK versus...',
	# 	   'P': 'PAPER versus...',
	# 	   'S': 'SCISSOR versus...'}[playerMove])

	# Count to three with dramatic pauses
	time.sleep(0.5)
	print('1...')
	time.sleep(0.25)
	print('2...')
	time.sleep(0.25)
	print('3...')
	time.sleep(0.25)

	# Display what the computer chose
	randomNumber = random.randint(1, 3) # or random.choice(['ROCK', 'PAPER', 'SCISSOR'])
	if randomNumber == 1:
		computerMove = 'ROCK'
	elif randomNumber == 2:
		computerMove = 'PAPER'
	else:
		computerMove = 'SCISSOR'
	print(computerMove)

	# Display and record the win/loss/tie:
	# Tie condition
	if playerMove == computerMove:
		print('It\'s a tie!')
		ties += 1

	# Win condition
	elif playerMove == 'ROCK' and computerMove == 'SCISSOR':
		print('You win!')
		wins += 1
	elif playerMove == 'PAPER' and computerMove == 'ROCK':
		print('You win!')
		wins += 1
	elif playerMove == 'SCISSOR' and computerMove == 'PAPER':
		print('You win!')
		wins += 1

	# Lose condition
	elif playerMove == 'ROCK' and computerMove == 'PAPER':
		print('You lose!')
		losses += 1
	elif playerMove == 'PAPER' and computerMove == 'SCISSOR':
		print('You lose!')
		losses += 1
	elif playerMove == 'SCISSOR' and computerMove == 'ROCK':
		print('You lose!')
		losses += 1

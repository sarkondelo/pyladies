from random import randrange
while True:
	number = randrange (3)
	man_move = input("Rock, paper, scissors or end? ")
	if number == 0:
		pc_move = 'rock'
	elif number == 1:
		pc_move = 'scissors'
	elif number == 2:
		pc_move = 'paper'
	else:
		print ("I don't understand.")
	print ('PC move: ', pc_move)
	print ('Your move: ', man_move)
	if pc_move == man_move:
		print ("Equal.")
	elif (pc_move == 'rock' and man_move == 'paper') or (pc_move == 'paper' and man_move == 'scissors') or (pc_move == 'scissors' and man_move == 'rock'):
		print ('You win.')
	elif (pc_move == 'rock' and man_move == 'scissors') or (pc_move == 'scissors' and man_move == 'paper') or (pc_move == 'paper'and man_move == 'rock'):
		print ("You lose.")
	elif man_move == 'end':
		break
	else:
		print("I don't uderstand.")
print ('Thanks for the game!')

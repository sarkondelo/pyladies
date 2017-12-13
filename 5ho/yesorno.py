def yes_or_no(question):
	'Asks a question and returns True or False according to the answer.'
	while True:
		answer = input(question)
		if answer in ('yes', 'y', 'y'.upper()):
			return True
		elif answer in ('no', 'n', 'n'.upper()):
			return False
		else:
			print('I dont understand, answer yes, no or y, n.')
	print(yes_or_no('Do you want to continue? '))

if yes_or_no('Do you want to play a game? '):
	print('OK! But first, you have got to program it!')
else:
	print('Pity.')



def yes_or_no(question):
	'Asks a question and returns True or False according to the answer.'
	while True:
		answer = input(question)
		if answer == 'yes':
			return True
		elif answer == 'no':
			return False
		else:
			print('I dont understand, answer yes or no.')
	print(yes_or_no('Do you want to continue? '))
if yes_or_no('Do you want to play a game? '):
	print('OK! But first, you have got to program it!')
else:
	print('Pity.')

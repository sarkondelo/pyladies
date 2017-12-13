#funkce, která se zeptá na příjmení
#if 3 last letters are "ová" or last one letter "ů", it is a woman
#ask if its true
#if no, apologize
pes = input("What's your last name? ")

def lastname(question):
	if 'ová' in question:
		print ('You are a woman!')
	elif 'ů' in question:
		print ('You are a woman!')
	else:
		print ('You are a man!')

lastname(pes)


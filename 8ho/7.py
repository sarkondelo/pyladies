birth_number = input('Zadej svoje rodné číslo, prosím. ')

#fce analytující formát rč
def format(birth_number):
	intak = int(birth_number[:6])
	intak2 = int(birth_number[-4:])
	if len(str(intak)) == 6 and birth_number[6] == '/' and len(str(intak2)) == 4:
		return True
	else:
		return False
print(format(birth_number))

#dělitelné jedenácti
def eleven(birth_number):
	if birth_number % 11 == 0:
		return True
	else:
		return False

#vrátí datum narození ve formátu třech čísel - 08, 07, 97
#def date_of_birth(birth_number):
#	day = birth_number[4:5]
#	month = int(birth_number[2:3])
#	year = int(birth_number[0:1])
#	return date_of_birth(birth_number)
#print(date_of_birth(birth_number))

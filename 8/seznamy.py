# in list 2, 3, 4, 5, 6, 7, 8, 9, J, K, Q, A

#list(range(2,10))
import random

hodnoty = ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']
barvy = ['Srdce', 'Káry', 'Kříže', 'Piky']

balicek = []
for hodnota in hodnoty:
	for barva in barvy:
		balicek.append(hodnota + ' ' + barva)
random.shuffle(balicek)

#print('Karty prvního hráče jsou: ')
#for player1 in range(5):
#	print(balicek.pop())
#print ('Karty druhého hráče jsou: ')
#for player2 in range(5):
#	print(balicek.pop())
#print ('Karty v balíčku jsou: ')
#print (balicek)

ruce = []

for cislo_hrace in range(5):
	ruka=[]
	for cislo_karty in range(5):
		ruka.append(balicek.pop())
	ruce.append(ruka)

for cislo_hrace in range(5):
	print ('Hráč', cislo_hrace, 'má: ', ruce[cislo_hrace])

print(ruce)
print('V balíčku zbylo', len(balicek), 'karet')

from random import randrange

def vyhodnot(pole):
	'vrati kod podle stavu hry'
    #pole je napr ------x--o---xxx---
	if 'xxx' in pole:
		return 'x'
	elif 'ooo' in pole:
		return 'o'
	elif '-' not in pole:
		return '!'
	else:
		return '-'

def tah(pole, cislo_policka, symbol):
	'vrati herni pole s danym symbolem umistenym na danou pozici'
	return (pole[:cislo_policka] + symbol + pole[cislo_policka+1:])

def tah_pocitace(pole):
	'vrati herni pole se zaznamenanym tahem pocitace'
	pozice = randrange (0,20)
	if '-' not in pole:
		raise ValueError('Není kam hrát!')
	while True:
		if pole[pozice] == '-':
			return tah(pole, pozice, 'x')
	
def tah_hrace(pole):
	while True:
		try:
			pozice=int(input('Na jaké pole chceš hrát? '))
			if pozice < 0:
				print('zaporna policka nejsou')
			elif pozice >= len(pole):
				print('to je moc')
			elif pole[pozice] != '-':
				print('tam uz to nejde')
			else:
				break
		except ValueError:
			print ('to neni cislo')
	return tah(pole, pozice, 'o')

def piskvorky1d():
	pole = '-' * 20
	while True:
		pole = tah_hrace(pole)
		print (pole)
		vyhodnoceni = vyhodnot(pole)
		pole = tah_pocitace(pole)
		vyhodnot(pole)
		if vyhodnot(pole) != '-':
			break
	print(pole)
	print('Vyhrál', vyhodnot(pole))





VELIKOST_POLE = 20

def over_cislo(cislo):
	if 0<= cislo < VELIKOST_POLE:
		print('OK')
	else:
		raise ValueError('Číslo nesmí být záporné!')

class Kocka:
	def __init__(self, jmeno):
		self.jmeno = jmeno
		self.pocet_zivotu = 9

	def je_ziva(self):
		return self.pocet_zivotu > 0

	def zamnoukej(self):
		print('{}: Mňau'.format(self.jmeno))

	def vypis_pocet_zivotu(self):
		print('{}: má'.format(self.jmeno), self.pocet_zivotu, 'životů.'.format(self.pocet_zivotu))

	def uber_zivot(self):
		if self.pocet_zivotu == 0:
			print('Kočka už je mrtvá.')
			return
		self.pocet_zivotu = self.pocet_zivotu - 1

	def snez(self, jidlo):
		if self.pocet_zivotu == 0:
			print ('Mrtvá kočka nejí.')
			return
		if jidlo == 'ryba':
			if self.pocet_zivotu >=9:
				print('Kočka nemůže mít více životů.')
			else:
				print('Kočka snědla rybu.')
				self.pocet_zivotu = self.pocet_zivotu + 1
		else:
			print('Kočka jí jídlo ({})'.format(jidlo))
		

micka = Kocka('Micka')
print(micka.zamnoukej())
print(micka.vypis_pocet_zivotu())
micka.uber_zivot()
micka.snez('ryba')



class Zviratko:
	def __init__(self, jmeno):
		self.jmeno = jmeno
	def snez(self, jidlo):
		print('{}: Ňam, {} mi chutná!'.format(self.jmeno, jidlo))
	def udelej_zvuk(self):
		print('{} dělá zvuk'.format(self.jmeno))

class Kotatko(Zviratko):
	def zamnoukej(self):
		print('{}: Mňau'.format(self.jmeno))
	def snez(self, jidlo):
		print('{} se na {} chvíli kouká.'.format(self.jmeno, jidlo))
		super().snez(jidlo)

class Hadatko(Zviratko):
	def __init__(self, jmeno):
		jmeno = jmeno.replace('s', 'sss')
		jmeno = jmeno.replace ('S', 'Sss')
		super().__init__(jmeno)
	def udelej_zvuk(self):
		print('{}: Ssssssssss'.format(self.jmeno))

class Stenatko(Zviratko):
	def zastekej(self):
		print('{}: Haf!'.format(self.jmeno))

class Vcelka(Zviratko):
	def __init__(self):
		super().__init__('Mája')
	def udelej_zvuk(self):
		print('{}: Bzzzzzz'.format(self.jmeno))


micka = Kotatko ('Micka')
azorek = Stenatko ('Azorek')
standa = Hadatko('Stanislav')
micka.zamnoukej()
azorek.zastekej()
maja = Vcelka()

zviratka = [micka, azorek, standa, maja]
for zviratko in zviratka:
	zviratko.snez('maso')
	zviratko.udelej_zvuk()

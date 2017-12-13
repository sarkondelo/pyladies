
# ntici používám jen v případě, že vím, kolik tam bude prvků
# např fce ze které chci vrátit dvě hodnoty najednou

def podil_a_zbytek(a, b):
	return a//b, a%b

podil, zbytek = podil_a_zbytek(5, 3)

print('Podil je', podil)
print('Zbytek je', zbytek)

seznam_dvojic = []
for i in range(10):
	seznam_dvojic.append( (i, 2**i) ) #závorka znázorní pro python ntici, append bere jeden argument a bez závorky to pyth bere jako dva

print(seznam_dvojic)

for cislo, dve_na_cislo in seznam_dvojic:
	print('Dvě na', cislo, 'je', dve_na_cislo)

osoby = ['máma', 'teta', 'babička', 'vrah']
vlastnosti = ['hodná', 'milá', 'laskavá', 'zákeřný']
for osoba, vlastnost in zip(osoby, vlastnosti):
	print(vlastnost, osoba)

for cislo, osoba in enumerate(osoby):
	print('osoba číslo', cislo + 1, 'je', osoba)


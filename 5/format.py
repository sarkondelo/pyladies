a = 3
b = 4
vypis = "{0}x{1} = {2}".format(a, b, a*b)

print(vypis)

print("Ahoj,{jmeno}!".format(jmeno="Esmeraldo"))

def zamen(retezec, pozice, znak):
	zacatek = retezec[:pozice]
	prostredek = znak
	konec = retezec[pozice+1:]
	return zacatek + prostredek + konec
print(zamen('palec', 0, 'v'), 'valec')
print(zamen('valec', 2, 'j'), 'vajec')

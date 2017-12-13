print ('Ahoj světe')

def obsah_ctverce(strana):
	obsah = strana ** 2
	return obsah
for x in range(5):
	print('Obsah čtverce se stranou', x, 'je', obsah_ctverce(x))

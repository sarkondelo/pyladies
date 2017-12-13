radky = []
for x in range(10):
	#make line
	radek = []
	for y in range(10):
		radek.append('.')
	# add to line list
	radky.append(radek)

#nastavit tečku na X
radek = radky[8]
radek[7] = 'X'
radky [7] [6] = 'O'


for radek in radky:
	for cislo in radek:
		print(cislo, end=' ')
	print()

#make line
radek = []
for y in range(10):
	radek.append('.')
# add to line list
radky = [radek] * 8
radek[7] = 'X'


for radek in radky:
	for cislo in radek:
		print(cislo, end=' ')
	print()

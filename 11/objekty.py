a = 'abc'
b = 'def'

def count(retezec, znak):
	pocet = 0
	for c in retezec:
		if c == znak:
			pocet = pocet + 1
	return pocet

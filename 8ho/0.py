animals = ['pes', 'kočka', 'opice', 'králík', 'had', 'andulka']
animals2 = ['pes', 'kočka', 'opice', 'slon', 'žížala']

#funkce, která vypíše jména zvířat kratší než pět písmen
def lenght(animals):
	short = []
	for animal in animals:
		if len(animal) <=5:
			short.append(animal)
	return short
print(lenght(animals))

#fce, která vypíše zvířata začínající na k
def starts_with_k(animals):
	initial_k = []
	for animal in animals:
		if 'k' in animal [0]:
			initial_k.append(animal)
	return initial_k
print(starts_with_k(animals))

#fce, která zjistí, jestli je slovo v seznamu zvířat nebo ne
def word_in_list(animals):
	word = input('Napiš zvíře a já ti řeknu, jestli je na seznamu. ')
	if word in animals:
		return True
	else:
		return False
print(word_in_list(animals))

#fce dostane dva seznamy, vrátí tři: zvířata v obou seznamech, zv. v prvním, zv. v druhém
def sorting(animals, animals2):
	in_both = []
	just_in_first = []
	just_in_second = []
	for animal in animals:
		if animal in animals2:
			in_both.append(animal)
		else:
			just_in_first.append(animal)	
	for animal in animals2:
		if animal no in animals:
			just_in_second.append(animal)
	return in_both, just_in_first, just_in_second

print(animals)
print(animals2)
for i in range (2):
	print(sorting(animals, animals2))


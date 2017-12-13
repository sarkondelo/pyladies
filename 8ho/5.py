animals = ['pes', 'kočka', 'opice', 'králík', 'had', 'andulka']

#seřadit seznam podle abecedy
print(sorted(animals)) #nezapomínat volat, tj. print

#funkce, která seřadí zvířata podle abecedy, ale bude ignorovat první písmeno
new_animals = [] #prázdný seznam

for animal in animals: 
	prvek = animal[1:], animal #vytiskne zvíře bez prvního písmena a s prvním písmenem
	new_animals.append(prvek) #přidá se do seznamu

new_animals.sort() #seřadí seznam podle abecedy
animals = [] #nový prázdný seznam
for key, animal in new_animals: #klíč - zvíře bez iniciály v seznamu nova_zvirata
	animals.append(animal) #přidá se do nového seznamu

print(animals) #vytiskne finální seznam

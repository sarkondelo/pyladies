lowest=0xFFFF #nejmenší možná hodnota
for i in range(4):
	foo = int(input('Input number, please: '))
	if foo < lowest:
		lowest = foo
print (lowest)

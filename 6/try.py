odpoved = input('Input a number. ')
#try blok co nejmenší
try:
	cislo = int(odpoved)
except ValueError:
	print('Not a number!')
else:
	print('Number is', number)
except Exception:
	print('Mistake!')
except TypeError:
	print('Typing error!')
finally:
	print('This will do always.')
print('OK')

#chyby voláme jen když víme, jaká chyba může nastat a jak ji ošetřit


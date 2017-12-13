from math import sqrt
from turtle import forward, left, right, exitonclick

side = int(input('Zadej velikost domečku. '))


def domecek(side, diagonal, roof):
	forward(side)
	left(90)
	forward(side)
	left(135)
	forward(diagonal)
	left(225)
	forward(side)
	left(270)
	forward(side)
	left(135)
	forward(roof)
	left(90)
	forward(roof)
	left(90)
	forward(diagonal)
	left(45)
	forward(25)
	return domecek
for i in range(3):
	side
	diagonal = side*sqrt(2)
	roof = diagonal/2
	domecek(side, diagonal, roof)
	side = side*2

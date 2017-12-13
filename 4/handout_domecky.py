from turtle import forward, left, right, exitonclick
from math import sqrt
side = 50
diagonal = side*sqrt(2)

for i in range (5):
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
    forward(35)
    left(90)
    forward(35)
    left(90)
    forward(diagonal)
    left(45)
    forward(25)

exitonclick()

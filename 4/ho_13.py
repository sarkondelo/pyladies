from turtle import forward, left, right, circle, exitonclick
from random import randrange

for i in range(10):
    type = randrange(0,3)
    if type == 0:
        left(90)
        forward(50)
        right(90)
        forward(25)
        right(90)
        forward(50) #první domeček
    elif type == 1:
        left(90)
        forward(200)
        right(90)
        forward(20)
        right(90)
        forward(200) #druhý domeček
    else: #2
        left(90)
        forward(100)
        right(90)
        forward(150)
        right(90)
        forward(100) #třetí domeček
    left(90)
    forward(20)
exitonclick()

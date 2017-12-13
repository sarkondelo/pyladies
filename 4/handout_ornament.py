from turtle import forward, left, penup, pendown, exitonclick

for i in range(40):
    forward (2*i)
    left(90)
penup()
forward(250)
pendown()
for j in range(40):
    forward(2*j)
    left(60)
exitonclick()

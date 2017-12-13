from turtle import forward, left, exitonclick

n = int(input('How many angles?: '))

for i in range(n):
    forward(200/n)
    left(360/n)
exitonclick()

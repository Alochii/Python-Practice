import turtle as t
import random as r

tim = t.Turtle()
tim.speed(0)
tim.pensize(1)
tim.color("purple")
def drawspiral(turtle, gap):
    for _ in range(1,int(360/gap) +1):
        turtle.circle(100)
        turtle.left(gap)


drawspiral(tim,1)

t.getscreen()
t.exitonclick()
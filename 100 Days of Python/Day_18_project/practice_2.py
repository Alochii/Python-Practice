import turtle as t
import random as r

t.colormode(255)
def randomwalk(turtle):
    for _ in range(20):
        turtle.color(randomcolor())
        direction = r.randint(0, 3)
        print(direction)
        turtle.right(directions[direction])
        turtle.forward(20)

def randomcolor():
    red = r.randint(0,255)
    green = r.randint(0,255)
    blue = r.randint(0,255)
    return (red, green, blue)
directions = [0, 90, 180, 270]

tim = t.Turtle()
tim.pensize(10)
tim.speed(0)

alex = t.Turtle()
alex.pensize(10)
alex.speed(0)

randomwalk(tim)
randomwalk(alex)


t.exitonclick()
t.getscreen()

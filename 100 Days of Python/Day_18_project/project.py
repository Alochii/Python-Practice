import turtle as t
import random as r
colors = [(212,185,214),(154,232,57),(250,150,60),(60,150,200),(10,20,232)]
# initialise information
t.colormode(255)


def artpiece(turtle,num):
    turtle.hideturtle()
    turtle.penup()
    turtle.speed(0)
    turtle.goto(-250, -250)
    turtle.shape("circle")
    turtle.pensize(15)
    turtle.shapesize(10/num)
    for rows in range (num):
        for stamps in range (num):
            turtle.color((r.randint(200,255),r.randint(0,255),r.randint(0,255)))
            turtle.stamp()
            turtle.forward(500/num)
        turtle.left(90)
        turtle.forward(500/num)
        turtle.right(90)
        turtle.back(500)

tim = t.Turtle()
artpiece(tim,10)



t.exitonclick()
t.getscreen()



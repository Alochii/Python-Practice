import turtle

tim = turtle.Turtle()

def moveforward():
    tim.forward(10)
screen = turtle.Screen()
screen.listen()
screen.onkey(key="a",fun= moveforward )
turtle.exitonclick()
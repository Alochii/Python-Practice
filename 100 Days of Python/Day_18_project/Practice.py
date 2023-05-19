import turtle
def centrecoords(turtle,sides):
    x1 = tim.xcor()
    y1 = tim.xcor()
    print (x1,y1)
    tim.penup()
    print(turtle.position())
    if sides % 2 == 0:
        turns = sides / 2
    else :
        turns = (sides + 1) / 2
    for _ in range(int(turns)):
        tim.forward(50)
        tim.right(360 / sides)
        lastturn = 360 / sides
    for _ in range(int(sides - turns)):
        tim.right(lastturn)
    print(turtle.position())
    x2 = tim.xcor()
    y2 = tim.ycor()
    print(x2,y2)
    if sides % 2 == 0:
        x3 = (x1 + x2) / 2
        y3 = (y1 + y2) / 2
    else:
        x3 = x2
        y3 = (y1 + y2) / 2
    print(x3,y3)
    tim.setpos(-x3,-y3)
    print(turtle.position())
    tim.pendown()


def drawshape(turtle, sides):
    for _ in range(sides):
        tim.forward(50)
        tim.right(360 / sides)
    tim.penup()
    tim.setpos(0,0)
    tim.pendown()




tim = turtle.Turtle()
tim.speed(0)
for _ in range(3,65):
    centrecoords(tim,_)
    drawshape(tim,_)
'''


distance = 200
for sides in range(3,6):
    print(sides)
    distance *= 0.86
    for _ in range(sides):

        tim.forward(distance)
        tim.right(360/sides)
    tim.forward(distance*0.07)
'''
turtle.exitonclick()
turtle.getscreen()

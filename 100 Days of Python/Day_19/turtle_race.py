import turtle as tur
import random
colors = ["red","orange","green","yellow","blue","purple","black"]
turtles = []

screen = tur.Screen()
screen.setup (width=800, height=420)

index = 0
ycoords = -180
winnercoords = -370
for index in range(7):
    new_turtle = tur.Turtle(shape="turtle")
    new_turtle.pensize(20)
    new_turtle.color(colors[index])
    new_turtle.penup()
    print(new_turtle.pencolor())
    new_turtle.goto(-370, ycoords)
    ycoords += 60
    turtles.append(new_turtle)


user_bet = screen.textinput("The grand prix Turtle race","enter the color of the turtle you want to bet on")

while True :
    randindex = random.randint(0,6)
    turtles[randindex].forward(random.randint(0,10))
    if turtles[randindex].xcor() > winnercoords:
        print(turtles[randindex].xcor())
        winnercoords = turtles[randindex].xcor()
        winner = turtles[randindex].pencolor()
    if winnercoords >= 350:
        print(f"the winner is {winner}")
        break

if winner == user_bet:
    print("you wont the bet!")
else :
    print("you lose the bet")
screen.exitonclick()
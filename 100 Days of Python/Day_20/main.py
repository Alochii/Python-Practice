import turtle
import snake
import time
import food
import scoreboard
screen = turtle.Screen()
screen.title("my snake game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snakegame = snake.Snake()

snakegame.NewSegment()
screen.listen()
screen.onkey(snakegame.up,"w")
screen.onkey(snakegame.down,"s")
screen.onkey(snakegame.left,"a")
screen.onkey(snakegame.right,"d")

foodbit = food.Food()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snakegame.SnakeMove()
    if snakegame.segments[0].distance(foodbit) < 15:
        foodbit.refresh()
        snakegame.extend()
        scoreboard.ScoreBoard().addpoints()
    xcor = snakegame.segments[0].xcor()
    ycor = snakegame.segments[0].ycor()
    if xcor > 280 or xcor < -280 or ycor >280 or ycor < -280 :
        game_is_on = False

    for segment in snakegame.segments[1:]:
        if snakegame.segments[0].distance(segment) < 10:
            game_is_on = False

scoreboard.ScoreBoard().gameover()
screen.exitonclick()
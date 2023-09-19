from turtle import Screen
import Paddle
import time
import ball
import score

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 500)


bars = Paddle.Paddle()
bars.start()
bars.enemy()
screen.listen()
screen.onkey(bars.up1, "w")
screen.onkey(bars.down1, "s")
screen.onkey(bars.up2, "9")
screen.onkey(bars.down2, "6")
screen.tracer(0)


while True:
    game_speed = 10
    score.Score()
    dot = ball.Ball()
    dot.start()
    while dot.out_of_bounds():
        dot.forward(game_speed)
        dot.bounce()
        if dot.paddle_bounce():
            game_speed += 2
        time.sleep(0.05)
        screen.update()
        screen.exitonclick()

# done 2 : create and move paddle
# done 3 : create adversary paddle
# done 4 : create ball and move it
# done 5 : detect collision with wall and bounce ball
# done 6 : detect collision with paddle
# done 7 : detect when paddle misses
# done 8 : keep score

# Done 1 : Make the screen

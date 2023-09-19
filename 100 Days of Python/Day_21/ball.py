from turtle import Turtle
import Paddle
import random
import score


class Ball(Turtle):
    HEADING = random.randint(-60, 60)

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

    def start(self):
        self.setheading(Ball.HEADING)

    def bounce(self):
        if self.ycor() >= 225 or self.ycor() <= -220:
            self.setheading(360 - self.heading())

    def paddle_bounce(self):
        if 340 <= self.xcor() <= 365:
            if Paddle.Paddle.Range[0] - 10 < self.ycor() < Paddle.Paddle.Range[1] + 10:
                self.setheading(180 - self.heading() + random.randint(-30, 30))
                return True
        if -340 >= self.xcor() >= -365:
            if Paddle.Paddle.Rangeme[0] - 10 < self.ycor() < Paddle.Paddle.Rangeme[1] + 10:
                self.setheading(540 - self.heading() + random.randint(-30, 30))
                return True
        return False

    def out_of_bounds(self):
        if self.xcor() >= 380:
            self.color("black")
            self.goto(-999, -999)
            score.Score().add_me()
            return False
        elif self.xcor() <= -380:
            self.color("black")
            self.goto(-999, -999)
            score.Score().add_adv()

        else:
            return True

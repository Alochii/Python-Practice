from turtle import Turtle
from car_manager import CARS
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)

    def start_position(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def collision(self):
        for squares in CARS:
            if squares[0].distance(self) < 20 or squares[1].distance(self) < 20:
                return True
        return False

    def finishline(self):
        if self.ycor() > 280:
            return True
        else:
            return False

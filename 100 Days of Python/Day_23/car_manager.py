from turtle import Turtle
from random import randint, choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS = []


class CarManager:
    def __init__(self):
        self.square = None
        self.body = []
        self.square_color = choice(COLORS)
        self.square_ypos = randint(-260, 300)

    def square_init(self):
        self.square = Turtle()
        self.square.penup()
        self.square.shape("square")
        self.square.setheading(180)
        self.square.color(self.square_color)

    def square_state(self, initializer):
        for _ in range(2):
            self.square_init()
            position = ((250 + (_ * 20)), self.square_ypos)
            self.square.goto(position)
            self.body.append(self.square)
        CARS.append(self.body)
        if initializer:
            self.initializer()
        self.body = []
        self.square_color = choice(COLORS)
        self.square_ypos = randint(-260, 280)

    def initializer(self):
        forward_distance = randint(-100, 700)
        self.body[0].forward(forward_distance)
        self.body[1].forward(forward_distance)

    def cars_move(self):
        for squares in CARS:
            squares[0].forward(STARTING_MOVE_DISTANCE)
            squares[1].forward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        global STARTING_MOVE_DISTANCE
        global MOVE_INCREMENT
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

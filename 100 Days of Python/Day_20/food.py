import turtle
import random
class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed(0)
        self.refresh()
    def refresh(self):
        x_coords = random.randint(-14, 14) * 20
        y_coords = random.randint(-14, 14) * 20
        self.goto(x_coords, y_coords)
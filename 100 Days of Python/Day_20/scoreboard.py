import turtle
class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)

    def updatescreen(self,points):
        self.clear()
        self.write(f"Current score : {points}", False, "center", font=('Arial', 12, 'normal'))
    def addpoints(self):
        self.points += 1
        self.updatescreen(self.points)

    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, "center", font=('Arial', 24, 'normal'))





from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        with open("Highscore.txt") as HIGHSCORE:
            self.highscore = int(HIGHSCORE.read())

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def high_score(self):
        if self.highscore < self.score:
            self.highscore = self.score
            with open("Highscore.txt", "w") as HIGHSCORE:
                HIGHSCORE.write(str(self.highscore))

            self.score = 0
            self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

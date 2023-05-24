from turtle import Turtle


class Score(Turtle):
    score1 = 0
    score2 = 0

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    def keep_score(self):
        self.clear()
        self.write(f"{Score.score1} | {Score.score2}", move=False, align='center', font=('Symbol', 70, 'normal'))

    def add_me(self):
        Score.score1 += 1
        self.keep_score()

    def add_adv(self):
        Score.score2 += 1
        self.keep_score()

from turtle import Turtle


class Paddle(Turtle):
    pieces = []
    advpieces = []
    Range = [-20, 20]
    Rangeme = [-20, 20]

    def __init__(self):
        super().__init__()
        self.initial_pos = [(-370, -20), (-370, 0), (-370, 20)]
        self.adversary_pos = [(370, -20), (370, 0), (370, 20)]

    def paddleshape(self, state):
        new_item = Turtle()
        new_item.shape("square")
        new_item.color("white")
        new_item.speed(0)
        new_item.penup()
        new_item.setheading(90)
        if state == 0:
            Paddle.pieces.append(new_item)
        elif state == 1:
            Paddle.advpieces.append(new_item)

    def start(self):
        for _ in range(3):
            self.paddleshape(0)
            self.pieces[_].goto(self.initial_pos[_])

    def enemy(self):
        for _ in range(3):
            self.paddleshape(1)
            self.advpieces[_].goto(self.adversary_pos[_])

    def paddlerange(self):
        Paddle.Range[0] = Paddle.advpieces[0].ycor()
        Paddle.Range[1] = Paddle.advpieces[2].ycor()

    def mypaddlerange(self):
        Paddle.Rangeme[0] = Paddle.pieces[0].ycor()
        Paddle.Rangeme[1] = Paddle.pieces[2].ycor()

    def up1(self):
        for piece in range(3):
            Paddle.pieces[piece].forward(20)
            self.mypaddlerange()

    def down1(self):
        for piece in range(3):
            Paddle.pieces[piece].forward(-20)
            self.mypaddlerange()

    def up2(self):
        for piece in range(3):
            Paddle.advpieces[piece].forward(20)
            self.paddlerange()

    def down2(self):
        for piece in range(3):
            Paddle.advpieces[piece].forward(-20)
            self.paddlerange()

import turtle
class Snake :
    def __init__(self):
        self.segments = []
        self.positions = [(0,0),(-20,0),(-40,0)]

    def NewSegment(self):
        for _ in self.positions:
            self.addsegment(_)

    def addsegment(self,_):
        new_segment = turtle.Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(_)
        self.segments.append(new_segment)

    def extend(self):
        self.addsegment(self.segments[-1].position())
    def SnakeMove(self):
        for index in range(len(self.segments) - 1, 0, -1):
            start = self.segments[index]
            # print(start.pos())
            end = self.segments[index - 1]
            # print(end.pos())
            start.goto(end.pos())
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
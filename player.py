STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=1)

        self.speed("fastest")
        self.goto(0,-280)
        self.setheading(90)
    def up(self):
        self.goto(self.xcor(),self.ycor()+MOVE_DISTANCE)
    def finish(self):
        if self.ycor()==FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
from turtle import Turtle
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.color(COLORS[random.randint(0,len(COLORS)-1)])
        self.speed("fastest")
        self.speed=MOVE_INCREMENT

        self.goto(random.randint(310, 350), random.randint(-260, 260))


    def move(self):
        self.goto(self.xcor()-self.speed,self.ycor())
    def setspeed(self,k):
        self.speed=MOVE_INCREMENT*k
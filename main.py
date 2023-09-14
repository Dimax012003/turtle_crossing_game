import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car=[]
k=0
lego=Player()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(lego.up,"Up")

game_is_on = True
w=1
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if k%2==0:
        p=CarManager()
        p.setspeed(w)
        car.append(p)
        for c in car:
            c.setspeed(w)
    for c in car:
        c.move()
    for c in car:
        if abs(lego.xcor()-c.xcor())<=10 and abs(lego.ycor()-c.ycor())<=10 :
            scoreboard.game_over()
            game_is_on=False
            screen.update()
            scoreboard.game_over()
            time.sleep(1)
    k=k+1
    if lego.finish():
        scoreboard.update()
        w=w+1

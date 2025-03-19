from turtle import Screen, Turtle
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong Game")
screen.tracer(0)

p1_position = (-350,0)
p2_position = (350,0)

p1 = Player(p1_position)
p2 = Player(p2_position)
screen.listen()
screen.onkey(p1.move_up, "w")
screen.onkey(p1.move_down, "s")
screen.onkey(p2.move_up, "Up")
screen.onkey(p2.move_down, "Down")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move(ball.movement)
    
    if ball.xcor() >380 or ball.xcor()<-380:
        game_is_on = False
        scoreboard.gameover()

screen.exitonclick()


#continue write the collision to upper and lower to bounce 
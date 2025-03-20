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
    ball.moving(ball.x_movement, ball.y_movement)
    
    if ball.xcor() >380:
        ball.reset_position()
    
    elif ball.xcor()<-380:
        ball.reset_position()        
        
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    
    # if p1.distance(ball.xcor())<10 or p2.distance(ball.xcor())<10:
    #     ball.bounce_x()
    
    if ball.distance(p1)<50 and ball.xcor()<-320 or ball.distance(p2)<50 and ball.xcor()>320:
        ball.bounce_x()

screen.exitonclick()


#continue write the collision to upper and lower to bounce 
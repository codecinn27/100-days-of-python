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
    time.sleep(ball.game_speed)
    ball.moving(ball.x_movement, ball.y_movement)
    
    #player 2 score a point
    if ball.xcor() >380:
        ball.increase_speed()
        scoreboard.p1_add_score()
        game_is_on = scoreboard.check_score()
        ball.reset_position()
    
    #player 1 score a point 
    elif ball.xcor()<-380:
        ball.increase_speed()
        scoreboard.p2_add_score()
        game_is_on = scoreboard.check_score()
        ball.reset_position()        
        
    # ball collide with the ball and change direction    
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    
    # when ball collide with player change the direction of ball to the opposite X direction
    if ball.distance(p1)<50 and ball.xcor()<-320 or ball.distance(p2)<50 and ball.xcor()>320:
        ball.bounce_x()

screen.exitonclick()


#continue write the collision to upper and lower to bounce 
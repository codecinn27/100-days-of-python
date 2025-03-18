#update snake game to move the snake with keyboard keys

from turtle import Screen
import time 
from snake import Snake
from food import Food
import math
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) 

def run_game():
    global snake,food,scoreboard,game_is_on
    
    snake = Snake()
    # snake.speed(1) #slowest speed
    # snake.speed(0) #fastest speed
    food = Food()
    scoreboard = Scoreboard()
    
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right, "Right")
    game_is_on = True
    
    while game_is_on:
        screen.update()
        
        time.sleep(0.1)
        snake.move()   
        
        #detect collision food and snake
        if snake.head.distance(food) <20:
            # print("Detect")
            food.refresh()
            scoreboard.increase_score()
            snake.increasel_length()
        
        #detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor()>280 or snake.head.ycor() <-280:
            game_is_on = False
            scoreboard.game_over()
            wait_for_restart()
            
        #detect collision with tail
        #using loop method
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) <10:
                game_is_on = False
                scoreboard.game_over()
                wait_for_restart()

def wait_for_restart():
    scoreboard.restart()
    screen.listen()
    screen.onkey(restart_game,"y")
    screen.onkey(restart_game,"Y")
    
def restart_game():
    screen.clear()
    screen.tracer(0) 
    screen.bgcolor("black")
    run_game()
      
    
run_game()           

screen.exitonclick()
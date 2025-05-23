#update snake game to move the snake with keyboard keys

from turtle import Screen
import time 
from snake import Snake
from food import Food
import math

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

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
        print("Detect")
        food.refresh()
        
screen.exitonclick()
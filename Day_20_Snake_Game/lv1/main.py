from turtle import Screen, Turtle
import time 

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments =[]

for position in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments.append(segment)

game_is_on = True
while game_is_on:
    screen.update()
    
    # for seg_num in range(start=2, stop=0, step = -1 ):
    for seg_num in range(len(segments)-1, 0, -1 ):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    
    # for seg in segments:
    #     seg.forward(20)
    # time.sleep(1)   
        
screen.exitonclick()
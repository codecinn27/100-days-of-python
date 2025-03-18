from turtle import Turtle
import math

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.movement = None
        
    def create_snake(self):
        for position in STARTING_POSITION:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1 ):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.movement = "up"
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.movement = "down"
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.movement = "left"
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.movement = "right"
            
    def increasel_length(self):
        if self.movement == "left":
            last_position = len(self.segments)-1
            last_xcor = self.segments[last_position].xcor()
            last_ycor = self.segments[last_position].ycor()
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto((last_xcor,last_ycor))
            self.segments.append(segment)

        elif self.movement == "right":
            last_position = len(self.segments)-1
            last_xcor = self.segments[last_position].xcor()
            last_ycor = self.segments[last_position].ycor()
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto((last_xcor,last_ycor))
            self.segments.append(segment)
            
        elif self.movement == "up":
            last_position = len(self.segments)-1
            last_xcor = self.segments[last_position].xcor()
            last_ycor = self.segments[last_position].ycor()
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto((last_xcor,last_ycor))
            self.segments.append(segment)

        else:
            last_position = len(self.segments)-1
            last_xcor = self.segments[last_position].xcor()
            last_ycor = self.segments[last_position].ycor()
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto((last_xcor,last_ycor))
            self.segments.append(segment)

        
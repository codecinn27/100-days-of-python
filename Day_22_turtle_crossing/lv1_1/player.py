from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def up(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto((x_cor,y_cor+20))
        
    def down(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto((x_cor,y_cor-20))
        
    def left(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto((x_cor-20, y_cor))
        
    def right(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto((x_cor+20, y_cor))     
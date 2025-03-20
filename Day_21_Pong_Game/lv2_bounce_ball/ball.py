from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize()
        self.color("blue")
        self.movement = None
        self.x_movement = None
        self.y_movement = None
        self.random_movement()
        self.move(self.movement)
        
    def move(self, option):
        
        match option:
            case 1:
                self.x_movement = 15
                self.y_movement = 15 
                
            case 2:
                self.x_movement = 15
                self.y_movement = -15 
                
            case 3:
                self.x_movement = -15
                self.y_movement = -15 
                
            case 4:
                self.x_movement = -15
                self.y_movement = 15 
                
        
    def moving(self, x_m, y_m):
        new_x = self.xcor()+ x_m
        new_y = self.ycor() + y_m
        self.goto((new_x,new_y))
    
    def random_movement(self):
        temp = random.randint(3,4)
        self.movement = temp 
        
    def bounce_y(self):
        self.y_movement *=-1
    
    def bounce_x(self):
        self.x_movement *=-1
        
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
  
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
        self.random_movement()
        
    def move(self, option):
        
        match option:
            case 1:
                new_x = self.xcor()+ 15
                new_y = self.ycor() + 15
                self.goto((new_x,new_y))                
                
            case 2:
                new_x = self.xcor()+ 15
                new_y = self.ycor() - 15
                self.goto((new_x,new_y))
                
            case 3:
                new_x = self.xcor()- 15
                new_y = self.ycor() - 15
                self.goto((new_x,new_y))
                
            case 4:
                new_x = self.xcor()- 15
                new_y = self.ycor() + 15
                self.goto((new_x,new_y))
        
    def bounce(self):
        pass
    
    def random_movement(self):
        temp = random.randint(1,4)
        self.movement = temp 
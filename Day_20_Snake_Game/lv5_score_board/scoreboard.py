from turtle import Turtle
import random

class Scoreboard(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.score = 0
        self.refresh()

    def refresh(self):
        self.score +=1
        self.clear()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.write(f'Scoreboard: {self.score}', align="center", font=("Arial", 16, "bold"))

        

#when draw something always start with color -> penup->hideturtle -> goto -> write
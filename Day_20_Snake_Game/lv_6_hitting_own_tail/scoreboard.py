from turtle import Turtle
import random

ALIGNMENT = "center"
FONT =(("Arial", 16, "bold"))
FONT_GO =(("Arial", 30, "bold"))

class Scoreboard(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.score = 0
        self.write_score()
        
    def write_score(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.write(f'Scoreboard: {self.score}', align= ALIGNMENT, font= FONT)        

    def increase_score(self):
        self.score +=1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGNMENT, font= FONT)
        
    def restart(self):
        self.goto(0,30)
        self.write(f"Press Y to Restart", align=ALIGNMENT, font=FONT)
        

#when draw something always start with color -> penup->hideturtle -> goto -> write
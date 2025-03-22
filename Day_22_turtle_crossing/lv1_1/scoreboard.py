from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.draw()
    
    def draw(self):
        self.goto(-200,250)
        self.write(f"Level: {self.level}", align=ALIGNMENT , font=FONT)

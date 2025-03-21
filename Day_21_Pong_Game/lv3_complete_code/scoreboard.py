from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
FONT2 = ("Arial", 24, "bold")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.p1_write_score()
        self.p2_write_score()
        
    def gameover(self):
        self.write(f"Game over", align=ALIGNMENT , font=FONT)
        
    def p1_write_score(self):
        self.goto((-280, 200))
        self.write(self.p1_score, align=ALIGNMENT, font=FONT2)
        
    def p2_write_score(self):
        self.goto((280, 200))
        self.write(self.p2_score, align=ALIGNMENT, font=FONT2)
        
    def write_score(self):
        self.p1_write_score()
        self.p2_write_score()
        
    def p1_add_score(self):
        self.clear()
        self.p1_score +=1
        self.write_score()
        
    def p2_add_score(self):
        self.clear()
        self.p2_score +=1
        self.write_score()
     
    def check_score(self):
        if self.p1_score>3:
            self.p1_win()
            return False
        elif self.p2_score>3:
            self.p2_win()
            return False
        else:
            return True
            
    def p1_win(self):
        self.goto((0,0))
        self.write("P1 Win", align=ALIGNMENT, font=FONT2)
    
    def p2_win(self):
        self.goto((0,0))
        self.write("P2 Win", align=ALIGNMENT, font=FONT2)    
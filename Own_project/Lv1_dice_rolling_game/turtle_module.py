from turtle import Screen, Turtle
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Dice Game")

dice_faces = ["dice_gif/all.gif", 
              "dice_gif/1.gif", 
              "dice_gif/2.gif", 
              "dice_gif/3.gif", 
              "dice_gif/4.gif", 
              "dice_gif/5.gif" ,
              "dice_gif/6.gif" ,
              ]

# must add shape into the turtle before run the code prevent error
for img in dice_faces:
    screen.addshape(img)

dice_turtle = Turtle()
dice_turtle.penup()
dice_turtle.goto(0,0)
dice_turtle.shape(dice_faces[0])

def roll_dice():
    dice_no = random.randint(1,6)
    dice_turtle.shape(dice_faces[dice_no])
    
screen.listen()
screen.onkey(roll_dice,"space")

screen.mainloop()


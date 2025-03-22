from turtle import Turtle
import random 

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_speed = 18
        self.car = 10
        self.all_cars = []
        
        
    def random_spawn(self):    
        for x in range(self.car):
            self.spawn_car()
            
    def spawn_car(self):
        car = Turtle("square")
        car.shapesize(stretch_wid=3, stretch_len=1)
        car.penup()
        car.hideturtle()
        temp_color = random.choice(COLORS)
        car.color(temp_color)
        random_x_cor = random.randint(300,451)
        random_y_cor = random.randint(-280, 290)
        car.showturtle()
        car.goto((random_x_cor,random_y_cor))
        self.all_cars.append(car)
        
    
    def moving_car(self):
        for x in self.all_cars:
            x.backward(self.car_speed)

    def increase_car(self):
        self.car +=5
        
    def increase_car_speed(self):
        self.car_speed +=1
        
        
        


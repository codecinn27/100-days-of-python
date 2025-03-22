import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.up, "w")
screen.onkey(player.down, "Down")
screen.onkey(player.down, "s")
screen.onkey(player.left,"a")
screen.onkey(player.left,"Left")
screen.onkey(player.right,"d")
screen.onkey(player.right,"Right")
car_manager = CarManager()
car_manager.random_spawn()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.moving_car()
    

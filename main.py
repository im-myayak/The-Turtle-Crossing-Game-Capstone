import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(key="Up", fun=player.move)
game_is_on = True
count = 0
my_cars = {}
while game_is_on:
    time.sleep(scoreboard.game_speed)
    if count % 6 == 0:
        car_manager.create_car()
    car_manager.move_car()
    if player.is_level_completed():
        scoreboard.inc_level()
        car_manager.next_level()
        player.reset_turtle()
        count = -1
    for obj in car_manager.all_car:
        if player.distance(obj) < 25:
            scoreboard.game_over()
            game_is_on = False
    count += 1
    car_manager.car_passed()
    screen.update()


screen.exitonclick()
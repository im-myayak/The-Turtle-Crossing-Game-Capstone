import random as ran
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LESS = -250
MOST = 250
INITIAL_X = 300


class CarManager:
    def __init__(self):
        self.all_car = []
        self.moving_value = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.color(ran.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.up()
        ycor = ran.randint(LESS, MOST)
        new_car.goto(INITIAL_X, ycor)
        new_car.setheading(180)
        new_car.forward(self.moving_value)
        self.all_car.append(new_car)

    def next_level(self):
        self.moving_value += MOVE_INCREMENT

    def move_car(self):
        for obj in self.all_car:
            obj.forward(self.moving_value)

    def car_passed(self):
        for obj in self.all_car:
            if obj.ycor() <= -300:
                self.all_car.remove(obj)

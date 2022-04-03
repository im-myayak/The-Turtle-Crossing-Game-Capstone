from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.shapesize(stretch_wid=0.9, stretch_len=1)
        self.setheading(90)
        self.reset_turtle()

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def reset_turtle(self):
        self.goto(STARTING_POSITION)

    def is_level_completed(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.reset_turtle()
            return True
        return False


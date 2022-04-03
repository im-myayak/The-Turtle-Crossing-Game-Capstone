from turtle import Turtle

FONT = ("Courier", 24, "bold")
POSITION = (-250, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")

        self.up()
        self.hideturtle()
        self.pencolor("black")
        self.goto(POSITION)
        self.level = 1
        self.update_level()
        self.game_speed = 0.2

    def inc_level(self):
        self.level += 1
        # self.game_speed *= 0.5
        self.clear()
        self.update_level()

    def update_level(self):
        self.write(f"LEVEL: {self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

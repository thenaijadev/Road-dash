from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.life = 3
        self.level = 1
        self.penup()
        self.goto(-100, 250)
        self.hideturtle()
        self.write(f"Score: {self.score} Lives: {self.life} Level: {self.level}", align="center", font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.hideturtle()
        self.penup()
        self.write("GAME OVER", align="center", font=("Arial", 30, "normal"))

    def add_score(self):
        self.clear()
        self.score += 1
        self.level += 1
        self.write(f"Score: {self.score} Lives: {self.life} Level: {self.level}", align="center", font=FONT)

    def loss(self):
        self.clear()
        self.life -= 1
        self.write(f"Score: {self.score} Lives: {self.life} Level: {self.level}", align="center", font=FONT)

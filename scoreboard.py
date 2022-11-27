from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.number_states = 50
        self.number_guess = 0
        self.goto(-40, 300)
        self.write(self.number_guess, align="center", font=("Courier", 50, "normal"))
        self.goto(30,300)
        self.write(f"/{self.number_states}", align="center", font=("Courier", 50, "normal"))



    def update_scoreboard(self):
        self.clear()
        self.number_guess += 1
        self.goto(-40, 300)
        self.write(self.number_guess, align="center", font=("Courier", 50, "normal"))
        self.goto(30, 300)
        self.write(f"/{self.number_states}", align="center", font=("Courier", 50, "normal"))
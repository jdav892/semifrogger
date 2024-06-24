from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().init__()
        self.clear()
        self.goto(-250, 270)
        """add level method"""
        #self.write(self.level, FONT)
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level_number = 1
        self.update_level()
         
    def update_level(self):
        self.clear()
        self.goto(-200, 250)
        #self.write("Level: " + self.level_number, align="center", font=FONT)
    
    def level_up(self):
        self.level_number += 1
        self.update_level()
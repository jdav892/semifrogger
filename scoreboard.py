from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level_number = 1
        self.goto(-250, 265)
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level_number}", align="left", font=FONT)
    
    
    def increase_level(self):
        self.level += 1
        self.update_scoreboard() 
        
    def game_over_text(self):
        self.goto(0, 0)
        self.write(f"Game Over...", align="center", font=FONT)  
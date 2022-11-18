from turtle import Turtle

class Levels(Turtle):
    def __init__(self):
        super().__init__()
        self.level_count = 1
        
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        
    
    def update(self):
        self.clear()
        self.write(f"Level: {self.level_count}", move = False, align = "left", font = ("Courier", 16, "bold"))
    
    def game_over(self):
        self.goto(0, -280)
        self.write("GAME OVER", move = True, align = "center", font = ("Courier", 16, "bold"))
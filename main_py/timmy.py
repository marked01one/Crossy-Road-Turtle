from turtle import Turtle

class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)
    
    def move(self):
        self.forward(20)
    
    def reset_position(self):
        self.goto(0, -280)
    
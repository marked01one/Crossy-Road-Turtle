from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "lime", "green", "aqua", "cyan", "blue", "purple", "pink"]

class Cars():
    def __init__(self):
        self.repository = []
        self.movement_speed = 5
        
    def new_car_line(self):
        for car in range(12):
            rng = random.randint(1,40)
            if rng == 40:
                car = Turtle()
                car.penup()
                car.shape("square")
                car.color(random.choice(COLORS))
                car.setheading(180)
                car.shapesize(stretch_len = 2, stretch_wid = 1)
                car.goto(280, random.randint(-230, 210))
                self.repository.append(car)
    
    def move_cars(self):
        for car in self.repository:
            car.forward(self.movement_speed)
            
    def increase_speed(self):
        self.movement_speed += 3
    
    def remove_excessive(self):
        for car in self.repository:
            if car.xcor() < -300:
                car.hideturtle()
                self.repository.remove(car)
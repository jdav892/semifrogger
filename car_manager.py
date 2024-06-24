from turtle import Turtle
import random 

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_POSITION = random.randint(15, 255)

class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        
    def create_cars(self):
        random_chance = random.randint(1, 10)
        if random_chance == 1:
            car_generator = Turtle("square")
            car_generator.shapesize(stretch_wid=1, stretch_len=2)
            car_generator.penup()
            car_generator.color(random.choice(COLORS))
            random_y = random.randint(-240, 250)
            car_generator.goto(300, random_y)
            self.all_cars.append(car_generator)
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
        
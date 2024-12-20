from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_Y_POSITIONS_RANGE = (-260,290)
STARTING_X_POSITION = 300

class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
    
    def new_car(self):
        rand_int = random.randint(0, 15)
        
        if rand_int % 7 == 0:
            car = Turtle()
            car.shape('square')
            car.shapesize(1, 2)
            car.penup()
            car.color(random.choice(COLORS))
            car.setposition(290, random.randint(*STARTING_Y_POSITIONS_RANGE))
            car.setheading(180)
            self.cars.append(car)
    
    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)
            if car.xcor() < -300:
                self.remove_car(car)
    
    def clear_cars(self):
        for car in self.cars:
            self.remove_car(car)
    
    def remove_car(self, car):
        self.cars.remove(car)
        car.reset()
    
    def increase_difficulty(self):
        self.move_distance += MOVE_INCREMENT

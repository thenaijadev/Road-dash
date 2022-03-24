import random
from turtle import  Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []


    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_cars = Turtle("square")
            new_cars.shapesize(stretch_wid=2, stretch_len=1)
            new_cars.color(random.choice(COLORS))
            new_cars.penup()
            new_cars.setheading(90)
            random_y = random.randint(-250, 300)
            new_cars.goto(300, random_y)
            self.all_cars.append(new_cars)
        self.move()

    def move(self):
        for car in self.all_cars:
            new_y = car.ycor()
            new_x = car.xcor() - 10
            car.goto(new_x, new_y)
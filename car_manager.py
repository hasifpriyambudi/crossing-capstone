from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allCars = []
        self.carSpeed = MOVE_INCREMENT

    def makeCar(self):
        chance = random.randint(1, 6)
        if chance == 1:
            randomY = random.randint(-250, 250)
            car = Turtle()
            car.shape("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(1, 2)
            car.setpos(320, randomY)
            self.allCars.append(car)

    def moveCar(self):
        for car in self.allCars:
            car.backward(self.carSpeed)

    def increaseSpeed(self):
        self.carSpeed += MOVE_INCREMENT

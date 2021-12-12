import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen Settings
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Player
player = Player()
screen.onkeypress(player.Up, "Up")
screen.onkeypress(player.Down, "Down")

# Car
car = CarManager()

# Score
score = Scoreboard()
score.score()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Make Car
    car.makeCar()
    car.moveCar()

    # Collides
    for carLoop in car.allCars:
        if carLoop.distance(player) < 25:
            game_is_on = False
            score.gameOver()

    # Finish
    if player.finishLine():
        player.resetPosition()
        score.increaseScore()
        car.increaseSpeed()

screen.exitonclick()

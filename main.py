import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from player import STARTING_POSITION
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()
screen.onkey(player.move, "Up")
new_car = CarManager()


game_is_on = True
pace = 0.1
while game_is_on:
    time.sleep(pace)

    new_car.create_car()

    screen.update()

    # Collision with car
    for car in new_car.all_cars:
        if car.distance(player) < 20:
            player.goto(STARTING_POSITION)
            scoreboard.loss()
            if scoreboard.life == 0:
                scoreboard.game_over()
                game_is_on = False


    # Player at the other end
    if player.success() is True:
        player.goto(STARTING_POSITION)
        scoreboard.add_score()
        pace *= 0.8

screen.exitonclick()



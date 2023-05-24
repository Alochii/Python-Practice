import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from random import randint


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


def game():
    car = CarManager()
    for _ in range(24):
        car.square_state(True)

    turtle = Player()
    turtle.start_position()
    screen.listen()
    screen.onkey(turtle.move, "w")
    screen.onkey(turtle.move, "8")
    game_is_on = True
    while game_is_on:
        if randint(1, 5) == 1:
            car.square_state(False)
        if turtle.collision():
            print("you lose")
            break
        if turtle.finishline():
            turtle.start_position()
            car.level_up()
        car.cars_move()
        time.sleep(0.1)
        screen.update()
    screen.clear()
    screen.tracer(0)


while True:
    game()
# DONE 1 : turtle spawns and moves up on key press
# DONE 2 : square spawns on screen
# DONE 3 : multiple squares spawn on random
# DONE 4 : collision of squares with the turtle
# Done 5 : level up and faster squares


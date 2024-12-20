import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

FINISH_LINE_Y_CORS = 290
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
scoreboard = ScoreBoard()


player = Player()
car_manager = CarManager()

screen.onkey(player.move, 'space')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.new_car()
    car_manager.move_cars()

    for car in  car_manager.cars:
        if ((player.ycor() < car.ycor() + 10 and player.ycor() > car.ycor() - 10)
        and player.distance(car) < 35):
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() >= FINISH_LINE_Y_CORS:
        car_manager.clear_cars()
        car_manager.increase_difficulty()
        scoreboard.level_up()
        player.refresh()
        
    screen.update()

screen.exitonclick()

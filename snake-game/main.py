from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()

game_is_on = True

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

# segments = []

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
scoreboard.setpos(0, 100)

screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_segment()
        scoreboard.refresh()
    
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280
    or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        game_is_on = False
        scoreboard.game_over()
    
    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
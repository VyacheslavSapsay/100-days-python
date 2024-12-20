from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

game_is_on = True
screen = Screen()
screen.setup(width=800, height=600)

screen.bgcolor('black')
screen.title('Pong Game')
screen.listen()
screen.tracer(0)


r_paddle = Paddle('right')
l_paddle = Paddle('left')

ball = Ball()

score_board = ScoreBoard()

screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

while game_is_on:
    ball.move()
    if (ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce()
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320
    or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
         ball.bounce_by_paddle()
    elif ball.xcor() > 390:
        ball.reset()
        ball = Ball(heading='to_left')
        score_board.r_point()
    elif ball.xcor() < -390:
        ball.reset()
        ball = Ball(heading='to_right')
        score_board.l_point()
        
    screen.update()

screen.exitonclick()
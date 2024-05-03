import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
screen.listen()

scoreboard = Scoreboard()

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >= 285 or ball.ycor() <= -285:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() < 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        ball.bounce_x()

    # R paddle
    if ball.xcor() >= 380:
        ball.reset_position()
        scoreboard.r_point()

    # L paddle
    if ball.xcor() <= -380:
        ball.reset_position()
        scoreboard.l_point()




screen.exitonclick()

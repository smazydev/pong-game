from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

R_POSITION = (350,0)
L_POSITION = (-350,0)


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)


r_paddle = Paddle(R_POSITION)
l_paddle = Paddle(L_POSITION)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect Colllision with the ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #Detect collisions with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #Detect when right paddle misses 
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_point()

    #Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_right_point()

screen.exitonclick()
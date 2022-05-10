from turtle import Screen
from sidebars import SideBars
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.tracer(0)
screen.listen()

top_bar = SideBars("top")
bottom_bar = SideBars("bottom")
bottom_bar = SideBars("left")
bottom_bar = SideBars("right")

b_paddle = Paddle(-350, 0, "sky blue")  # blue paddle
r_paddle = Paddle(350, 0, "red")  # red paddle

ball = Ball()

# for red paddle movement
screen.onkey(r_paddle.Up, "Up")
screen.onkey(r_paddle.down, "Down")

# for blue paddle movement
screen.onkey(b_paddle.Up, "w")
screen.onkey(b_paddle.down, "s")

scoreboard = ScoreBoard()

while True:
    time.sleep(0.02)

    scoreboard.UpdateScoreBoard()
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 240 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(b_paddle) < 50 and ball.xcor() < -320) or (ball.distance(r_paddle) < 50 and ball.xcor() > 320):
        # This side is blue paddle                               # This side is red Paddle
        ball.bounce_x()

    # miss r_paddle
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.resetPosition()

    # miss b_paddle
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.resetPosition()

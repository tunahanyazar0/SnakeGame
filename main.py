from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Score

#screen setups
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#snake
snake = Snake()

#screen listening
screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun=snake.left)

#food
food = Food()

#score
score = Score()

#game loop
control = True
while control:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision => turtle.distance(2.turtle)
    if snake.head.distance(food) < 15: #15 = kenarlarının yarıları toplamı
        food.refresh()
        score.increase_score()
        snake.add_segments()

    #detect with wall
    if snake.head.xcor() >300 or snake.head.xcor()<-300 or snake.head.ycor() >300 or snake.head.xcor()<-300:
        time.sleep(1)
        score.appendscore()
        score.reset()
        snake.reset()

    #detect with tail
    for i in snake.segments[1:]:
        if snake.head.distance(i) < 10:
            score.appendscore()
            score.reset()
            snake.reset()


screen.exitonclick()
